import pytest
from playwright.sync_api import expect

@pytest.fixture
def page(browser):
    page = browser.new_page()
    page.goto("https://demoqa.com/automation-practice-form")
    yield page
    page.close()

def test_invalid_first_name(page):
    nameField = page.locator("#firstName")
    nameField.fill("")
    page.fill("#lastName","Smith")
    page.fill("#userEmail","joe@somewhere.com")
    page.locator("input[type='radio'][value='Male']").check()
    page.fill("#userNumber","1234567890")
    page.click("#submit")
    expect(page.locator("#firstName:invalid")).to_have_count(1)
    expect(page.locator("#lastName:invalid")).to_have_count(0)
    expect(page.locator("#userEmail:invalid")).to_have_count(0)
    expect(page.locator("#gender-radio-1:invalid")).to_have_count(0)
    expect(page.locator("#userNumber:invalid")).to_have_count(0)

def test_invalid_last_name(page):
    nameField = page.locator("#lastName")
    nameField.fill("")
    page.fill("#firstName", "Joe")
    page.fill("#userEmail","joe@somewhere.com")
    page.fill("#userNumber","1234567890")
    page.locator("input[type='radio'][value='Male']").check()
    page.click("#submit")
    expect(page.locator("#lastName:invalid")).to_have_count(1)
    expect(page.locator("#firstName:invalid")).to_have_count(0)
    expect(page.locator("#userEmail:invalid")).to_have_count(0)
    expect(page.locator("#gender-radio-1:invalid")).to_have_count(0)
    expect(page.locator("#userNumber:invalid")).to_have_count(0)

def test_invalid_gender(page):
    page.fill("#firstName","Joe")
    page.fill("#lastName","Smith")
    page.fill("#userEmail","joe@somewhere.com")
    page.fill("#userNumber","1234567890")
    page.click("#submit")
    expect(page.locator("#gender-radio-1:invalid")).to_have_count(1)
    expect(page.locator("#lastName:invalid")).to_have_count(0)
    expect(page.locator("#firstName:invalid")).to_have_count(0)
    expect(page.locator("#userEmail:invalid")).to_have_count(0)
    expect(page.locator("#userNumber:invalid")).to_have_count(0)

def test_invalid_email(page):
    page.fill("#firstName","Joe")
    page.fill("#lastName","Smith")
    invalidField = page.locator("#userEmail")
    invalidField.fill("anything")
    page.fill("#userNumber","1234567890")
    page.locator("input[type='radio'][value='Male']").check()
    page.click("#submit")
    expect(page.locator("#userEmail:invalid")).to_have_count(1)
    expect(page.locator("#gender-radio-1:invalid")).to_have_count(0)
    expect(page.locator("#lastName:invalid")).to_have_count(0)
    expect(page.locator("#firstName:invalid")).to_have_count(0)
    expect(page.locator("#userNumber:invalid")).to_have_count(0)

def test_invalid_phone(page):
    page.fill("#firstName","Joe")
    page.fill("#lastName","Smith")
    page.fill("#userEmail","joe@somewhere.com")
    invalidField = page.locator("#userNumber")
    invalidField.fill("12345")
    page.locator("input[type='radio'][value='Male']").check()
    page.click("#submit")
    expect(page.locator("#userNumber:invalid")).to_have_count(1)
    expect(page.locator("#userEmail:invalid")).to_have_count(0)
    expect(page.locator("#gender-radio-1:invalid")).to_have_count(0)
    expect(page.locator("#lastName:invalid")).to_have_count(0)
    expect(page.locator("#firstName:invalid")).to_have_count(0)

def test_happy_path(page):
    page.fill("#firstName","Joe")
    page.fill("#lastName","Smith")
    page.fill("#userEmail","joe@somewhere.com")
    page.fill("#userNumber","1234567890")
    page.locator("input[type='radio'][value='Male']").check()
    page.click("#submit")
    success = page.locator('.modal-title')
    expect(success).to_be_visible