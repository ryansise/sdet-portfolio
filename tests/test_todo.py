import pytest
from playwright.sync_api import expect

@pytest.fixture
def todo_page(browser):
    page = browser.new_page()
    page.goto("https://todomvc.com/examples/react/dist/")
    yield page
    page.close()

def test_add_todo(todo_page):
    todo_page.fill(".new-todo", "Test KYC Workflow")
    todo_page.press(".new-todo", "Enter")
    todo_items = todo_page.locator("ul > li")
    expect(todo_items).to_contain_text(["Test KYC Workflow"])

