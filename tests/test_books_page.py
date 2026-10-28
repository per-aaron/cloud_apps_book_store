from playwright.sync_api import Page, expect
from database_connection import DatabaseConnection
from flask_bcrypt import Bcrypt
from app import app

def test_has_title(page: Page):
    page.goto("http://127.0.0.1:5001/books")

    h1 = page.locator("h1")

    expect(h1).to_have_text("Book List")

def test_has_book_list(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")
    page.goto("http://127.0.0.1:5001/books")

    #list = page.get_by_role("listitem")
    list = page.locator("li")
    books = list.all_inner_texts()

    assert books == ["The Gruffalo by Julia Donaldson",
                                "Ada Twist, Scientist by Andrea Beaty",
                                "The Girl Who Drank the Moon by Kelly Barnhill",
                                "Dragons in a Bag by Zetta Elliott"]

def test_unauth_user_cant_create_book(page: Page):
    bcrypt = Bcrypt(app)

    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    hashed = bcrypt.generate_password_hash('password123').decode('utf-8')
    connection.execute("INSERT INTO users (username, password) values ('testuser', %s)", [hashed])

    page.goto("http://127.0.0.1:5001/sessions/new")

    page.get_by_label("username").fill("testuser")
    page.get_by_label("password").fill("password1234")
    page.get_by_role("button", name="Sign in").click()
 
    page.goto("http://127.0.0.1:5001/books")
    page.get_by_label("Title").fill("The Spectre of Pep")
    page.get_by_label("Author").fill("Jon Mckenzie")
    page.get_by_role("button", name="Submit").click()

    list = page.locator("li")
    books = list.all_inner_texts()

    assert page.url == "http://127.0.0.1:5001/sessions/new"

def test_books_form_creates_book(page: Page):
    bcrypt = Bcrypt(app)

    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;") 
    hashed = bcrypt.generate_password_hash('password123').decode('utf-8')
    connection.execute("INSERT INTO users (username, password) values ('testuser', %s)", [hashed])

    page.goto("http://127.0.0.1:5001/sessions/new")

    page.get_by_label("username").fill("testuser")
    page.get_by_label("password").fill("password123")
    page.get_by_role("button", name="Sign in").click()

    page.goto("http://127.0.0.1:5001/books")

    page.get_by_label("Title").fill("Open Circuits")
    page.get_by_label("Author").fill("Windell Oskay")
    page.get_by_role("button", name="Submit").click()

    new_book = page.locator("li").all_inner_texts()[-1]

    assert new_book == "Open Circuits by Windell Oskay"


