from playwright.sync_api import Page, expect
from database_connection import DatabaseConnection
from flask_bcrypt import Bcrypt
from app import app

def test_successful_login_redirects_to_books(page: Page):
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

    #expect(page).to_have_url("http://127.0.0.1:5001/books") 
    assert page.url == "http://127.0.0.1:5001/books"

def test_incorrect_user_login_returns_to_new(page: Page):
    bcrypt = Bcrypt(app)

    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;") 
    hashed = bcrypt.generate_password_hash('password123').decode('utf-8')
    connection.execute("INSERT INTO users (username, password) values ('testuser', %s)", [hashed])

    page.goto("http://127.0.0.1:5001/sessions/new")

    page.get_by_label("username").fill("testuser2")
    page.get_by_label("password").fill("password123")
    page.get_by_role("button", name="Sign in").click()
 
    assert page.url == "http://127.0.0.1:5001/sessions/new"

def test_incorrect_pwd_login_returns_to_new(page: Page):
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
 
    assert page.url == "http://127.0.0.1:5001/sessions/new"