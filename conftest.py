from playwright.sync_api import sync_playwright
import pytest
from utils.configreader import ConfigReader
from pages.loginpage import LoginPage

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = ConfigReader.get_headless())
        yield browser
        browser.close()




@pytest.fixture(scope="function")
def context(browser):
    context= browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture
def logged_in_page(page):
    login = LoginPage(page)
    page.goto(ConfigReader.get_URL())
    login.login(ConfigReader.get_username(),ConfigReader.get_password())
    return page

