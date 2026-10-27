from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("http://127.0.0.1:5001/books")

    h1 = page.locator("h1")

    expect(h1).to_have_text("Book List")

def test_has_book_list(page: Page):
    page.goto("http://127.0.0.1:5001/books")

    #list = page.get_by_role("listitem")
    list = page.locator("li")
    books = list.all_inner_texts()

    assert books == ["The Gruffalo by Julia Donaldson",
                                "Ada Twist, Scientist by Andrea Beaty",
                                "The Girl Who Drank the Moon by Kelly Barnhill",
                                "Dragons in a Bag by Zetta Elliott"]
