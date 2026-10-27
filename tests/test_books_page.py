from playwright.sync_api import Page, expect
from database_connection import DatabaseConnection

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

def test_books_form_creates_book(page: Page):
    page.goto("http://127.0.0.1:5001/books")

    page.get_by_label("Title").fill("Open Circuits")
    page.get_by_label("Author").fill("Windell Oskay")
    page.get_by_role("button", name="Submit").click()

    new_book = page.locator("li").all_inner_texts()[-1]

    assert new_book == "Open Circuits by Windell Oskay"
