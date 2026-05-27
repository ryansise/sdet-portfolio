import pytest
from playwright.sync_api import expect

@pytest.fixture
def session(browser):
    page = browser.new_page()
    page.goto("https://todomvc.com/examples/react/dist/")
    yield page
    page.close()

def test_add_todo(session):
    session.fill(".new-todo", "Test KYC Workflow")
    session.press(".new-todo", "Enter")
    todo_items = session.locator("ul > li")
    expect(todo_items).to_contain_text(["Test KYC Workflow"])

