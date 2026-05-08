import pytest
from playwright.sync_api import sync_playwright, Playwright, expect

def test_add_todo(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    page.goto("https://todomvc.com/examples/react/dist/")
    page.fill(".new-todo", "Test KYC Workflow")
    page.press(".new-todo", "Enter")
    test_locator = page.locator("ul > li")
    expect(test_locator).to_contain_text(["Test KYC Workflow"])
    browser.close()

with sync_playwright() as playwright:
    test_add_todo(playwright)