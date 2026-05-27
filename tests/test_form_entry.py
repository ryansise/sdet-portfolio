import pytest
from playwright.sync_api import expect

@pytest.fixture
def form_page(browser):
    page = browser.new_page()
    page.goto("https://demoqa.com/automation-practice-form")
    yield page
    page.close()

@pytest.fixture
def valid_form_data():
    return {
        "first_name": "Joe",
        "last_name": "Smith",
        "user_email": "joe@somewhere.com",
        "user_number": "1234567890",
        "gender": "Male"
    }

def test_invalid_first_name(form_page,valid_form_data):
    form_page.fill("#lastName",valid_form_data["last_name"])
    form_page.fill("#userEmail",valid_form_data["user_email"])
    form_page.locator(f"input[type='radio'][value='{valid_form_data['gender']}']").check()
    form_page.fill("#userNumber",valid_form_data["user_number"])
    form_page.click("#submit")
    expect(form_page.locator("#firstName:invalid")).to_be_visible()
    expect(form_page.locator("#lastName:invalid")).to_have_count(0)
    expect(form_page.locator("#userEmail:invalid")).to_have_count(0)
    expect(form_page.locator("#gender-radio-1:invalid")).to_have_count(0)
    expect(form_page.locator("#userNumber:invalid")).to_have_count(0)

def test_invalid_last_name(form_page,valid_form_data):
    form_page.fill("#firstName",valid_form_data["first_name"])
    form_page.fill("#userEmail",valid_form_data["user_email"])
    form_page.fill("#userNumber",valid_form_data["user_number"])
    form_page.locator(f"input[type='radio'][value='{valid_form_data['gender']}']").check()
    form_page.click("#submit")
    expect(form_page.locator("#lastName:invalid")).to_be_visible()
    expect(form_page.locator("#firstName:invalid")).to_have_count(0)
    expect(form_page.locator("#userEmail:invalid")).to_have_count(0)
    expect(form_page.locator("#gender-radio-1:invalid")).to_have_count(0)
    expect(form_page.locator("#userNumber:invalid")).to_have_count(0)

def test_invalid_gender(form_page,valid_form_data):
    form_page.fill("#firstName",valid_form_data["first_name"])
    form_page.fill("#lastName",valid_form_data["last_name"])
    form_page.fill("#userEmail",valid_form_data["user_email"])
    form_page.fill("#userNumber",valid_form_data["user_number"])
    form_page.click("#submit")
    expect(form_page.locator("#gender-radio-1:invalid")).to_be_visible()
    expect(form_page.locator("#lastName:invalid")).to_have_count(0)
    expect(form_page.locator("#firstName:invalid")).to_have_count(0)
    expect(form_page.locator("#userEmail:invalid")).to_have_count(0)
    expect(form_page.locator("#userNumber:invalid")).to_have_count(0)

def test_invalid_email(form_page,valid_form_data):
    form_page.fill("#firstName",valid_form_data["first_name"])
    form_page.fill("#lastName",valid_form_data["last_name"])
    form_page.fill("#userNumber",valid_form_data["user_number"])
    form_page.fill("#userEmail","not-an-email")
    form_page.locator(f"input[type='radio'][value='{valid_form_data['gender']}']").check()
    form_page.click("#submit")
    expect(form_page.locator("#userEmail:invalid")).to_be_visible()
    expect(form_page.locator("#gender-radio-1:invalid")).to_have_count(0)
    expect(form_page.locator("#lastName:invalid")).to_have_count(0)
    expect(form_page.locator("#firstName:invalid")).to_have_count(0)
    expect(form_page.locator("#userNumber:invalid")).to_have_count(0)

def test_invalid_phone(form_page,valid_form_data):
    form_page.fill("#firstName",valid_form_data["first_name"])
    form_page.fill("#lastName",valid_form_data["last_name"])
    form_page.fill("#userEmail",valid_form_data["user_email"])
    form_page.locator(f"input[type='radio'][value='{valid_form_data['gender']}']").check()
    form_page.click("#submit")
    expect(form_page.locator("#userNumber:invalid")).to_be_visible()
    expect(form_page.locator("#userEmail:invalid")).to_have_count(0)
    expect(form_page.locator("#gender-radio-1:invalid")).to_have_count(0)
    expect(form_page.locator("#lastName:invalid")).to_have_count(0)
    expect(form_page.locator("#firstName:invalid")).to_have_count(0)

def test_happy_path(form_page,valid_form_data):
    form_page.fill("#firstName",valid_form_data["first_name"])
    form_page.fill("#lastName",valid_form_data["last_name"])
    form_page.fill("#userEmail",valid_form_data["user_email"])
    form_page.fill("#userNumber",valid_form_data["user_number"])
    form_page.locator(f"input[type='radio'][value='{valid_form_data['gender']}']").check()
    form_page.click("#submit")
    expect(form_page.locator(".modal-title")).to_be_visible()