from playwright.sync_api import Page, expect
from database_connection import DatabaseConnection

def test_successful_login_redirects_to_books(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;") 
    connection.execute("INSERT INTO users (username, password) values ('testuser', 'password123');")

    page.goto("http://127.0.0.1:5001/sessions/new")

    page.get_by_label("username").fill("testuser")
    page.get_by_label("password").fill("password123")
    page.get_by_role("button", name="Sign in").click()

    #expect(page).to_have_url("http://127.0.0.1:5001/books") 
    assert page.url == "http://127.0.0.1:5001/books"

def test_unsuccessful_login_returns_to_new(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;") 
    connection.execute("INSERT INTO users (username, password) values ('testuser', 'password123');")

    page.goto("http://127.0.0.1:5001/sessions/new")

    page.get_by_label("username").fill("testuser")
    page.get_by_label("password").fill("password1234")
    page.get_by_role("button", name="Sign in").click()
 
    assert page.url == "http://127.0.0.1:5001/sessions/new"