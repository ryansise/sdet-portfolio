# use https://demoqa.com/automation-practice-form

import pytest
from playwright.sync_api import sync_playwright, Playwright, expect

def test_kyc_ui(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    page.goto("https://demoqa.com/automation-practice-form")
    #nameField = page.fill("#firstName","")
    #errorIcon = nameField.locator(".form-control:invalid")
    page.fill("#lastName","Smith")
    page.fill("#userEmail","joe@somewhere.com")
    page.get_by_role("radio").filter(has_text="Male").click
    page.fill("#userNumber","123-456-7890")
    page.fill("#dateOfBirthInput","17 Nov 1980")
    page.fill("#subjectsInput","Linux")
    page.fill("#currentAddress","123 Main St")
    page.click("#submit")
    expect(errorIcon).to_be_visible()
    browser.close()

with sync_playwright() as playwright:
    test_kyc_ui(playwright)