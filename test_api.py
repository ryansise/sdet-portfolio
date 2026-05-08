import pytest
from playwright.sync_api import sync_playwright, Playwright, expect

def test_api(playwright: Playwright):
    context = playwright.request.new_context()
    response = context.get("https://jsonplaceholder.typicode.com/posts")
    expect(response).to_be_ok

with sync_playwright() as playwright:
    test_api(playwright)