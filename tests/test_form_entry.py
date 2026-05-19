# use https://demoqa.com/automation-practice-form

import pytest
from playwright.sync_api import sync_playwright, Playwright, expect

def test_invalid_firstName(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    page.goto("https://demoqa.com/automation-practice-form")
    nameField = page.locator("#firstName")
    nameField.fill("")
    page.fill("#lastName","Smith")
    page.fill("#userEmail","joe@somewhere.com")
    page.get_by_role("radio").filter(has_text="Male").click
    page.fill("#userNumber","1234567890")
    page.click("#submit")
    expect(page.locator("#firstName:invalid")).to_have_count(1)
    browser.close()

def test_invalid_lastName(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    page.goto("https://demoqa.com/automation-practice-form")
    nameField = page.locator("#lastName")
    nameField.fill("")
    page.fill("#firstName", "Joe")
    page.fill("#userEmail","joe@somewhere.com")
    page.get_by_role("radio").filter(has_text="Male").click
    page.click("#submit")
    expect(page.locator("#lastName:invalid")).to_have_count(1)
    browser.close()

def test_invalid_gender(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    page.goto("https://demoqa.com/automation-practice-form")
    page.fill("#firstName","Joe")
    page.fill("#lastName","Smith")
    page.fill("#userEmail","joe@somewhere.com")
    page.click("#submit")
    expect(page.locator("#gender-radio-1:invalid")).to_have_count(1)
    browser.close()

def test_invalid_email(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    page.goto("https://demoqa.com/automation-practice-form")
    page.fill("#firstName","Joe")
    page.fill("#lastName","Smith")
    invalidField = page.locator("#userEmail")
    invalidField.fill("anything")
    page.get_by_role("radio").filter(has_text="Male").click
    page.click("#submit")
    expect(page.locator("#userEmail:invalid")).to_have_count(1)
    browser.close()

with sync_playwright() as playwright:
    test_invalid_firstName(playwright)
    test_invalid_lastName(playwright)
    test_invalid_gender(playwright)
    test_invalid_email(playwright)