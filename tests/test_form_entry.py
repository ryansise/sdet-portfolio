import pytest
from playwright.sync_api import expect

@pytest.fixture
def form_page(browser):
    page = browser.new_page()
    page.goto("https://demoqa.com/automation-practice-form")
    yield page
    page.close()

def test_invalid_first_name(form_page):
    nameField = form_page.locator("#firstName")
    nameField.fill("")
    form_page.fill("#lastName","Smith")
    form_page.fill("#userEmail","joe@somewhere.com")
    form_page.locator("input[type='radio'][value='Male']").check()
    form_page.fill("#userNumber","1234567890")
    form_page.click("#submit")
    expect(form_page.locator("#firstName:invalid")).to_be_visible()
    expect(form_page.locator("#lastName:invalid")).to_have_count(0)
    expect(form_page.locator("#userEmail:invalid")).to_have_count(0)
    expect(form_page.locator("#gender-radio-1:invalid")).to_have_count(0)
    expect(form_page.locator("#userNumber:invalid")).to_have_count(0)

def test_invalid_last_name(form_page):
    nameField = form_page.locator("#lastName")
    nameField.fill("")
    form_page.fill("#firstName", "Joe")
    form_page.fill("#userEmail","joe@somewhere.com")
    form_page.fill("#userNumber","1234567890")
    form_page.locator("input[type='radio'][value='Male']").check()
    form_page.click("#submit")
    expect(form_page.locator("#lastName:invalid")).to_be_visible()
    expect(form_page.locator("#firstName:invalid")).to_have_count(0)
    expect(form_page.locator("#userEmail:invalid")).to_have_count(0)
    expect(form_page.locator("#gender-radio-1:invalid")).to_have_count(0)
    expect(form_page.locator("#userNumber:invalid")).to_have_count(0)

def test_invalid_gender(form_page):
    form_page.fill("#firstName","Joe")
    form_page.fill("#lastName","Smith")
    form_page.fill("#userEmail","joe@somewhere.com")
    form_page.fill("#userNumber","1234567890")
    form_page.click("#submit")
    expect(form_page.locator("#gender-radio-1:invalid")).to_be_visible()
    expect(form_page.locator("#lastName:invalid")).to_have_count(0)
    expect(form_page.locator("#firstName:invalid")).to_have_count(0)
    expect(form_page.locator("#userEmail:invalid")).to_have_count(0)
    expect(form_page.locator("#userNumber:invalid")).to_have_count(0)

def test_invalid_email(form_page):
    form_page.fill("#firstName","Joe")
    form_page.fill("#lastName","Smith")
    invalidField = form_page.locator("#userEmail")
    invalidField.fill("anything")
    form_page.fill("#userNumber","1234567890")
    form_page.locator("input[type='radio'][value='Male']").check()
    form_page.click("#submit")
    expect(form_page.locator("#userEmail:invalid")).to_be_visible()
    expect(form_page.locator("#gender-radio-1:invalid")).to_have_count(0)
    expect(form_page.locator("#lastName:invalid")).to_have_count(0)
    expect(form_page.locator("#firstName:invalid")).to_have_count(0)
    expect(form_page.locator("#userNumber:invalid")).to_have_count(0)

def test_invalid_phone(form_page):
    form_page.fill("#firstName","Joe")
    form_page.fill("#lastName","Smith")
    form_page.fill("#userEmail","joe@somewhere.com")
    invalidField = form_page.locator("#userNumber")
    invalidField.fill("12345")
    form_page.locator("input[type='radio'][value='Male']").check()
    form_page.click("#submit")
    expect(form_page.locator("#userNumber:invalid")).to_be_visible()
    expect(form_page.locator("#userEmail:invalid")).to_have_count(0)
    expect(form_page.locator("#gender-radio-1:invalid")).to_have_count(0)
    expect(form_page.locator("#lastName:invalid")).to_have_count(0)
    expect(form_page.locator("#firstName:invalid")).to_have_count(0)

def test_happy_path(form_page):
    form_page.fill("#firstName","Joe")
    form_page.fill("#lastName","Smith")
    form_page.fill("#userEmail","joe@somewhere.com")
    form_page.fill("#userNumber","1234567890")
    form_page.locator("input[type='radio'][value='Male']").check()
    form_page.click("#submit")
    success = form_page.locator('.modal-title')
    expect(success).to_be_visible()