import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
import time

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Cambia a True en CI
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="function")
def login_page(page):
    return LoginPage(page)


@pytest.fixture(scope="function")
def page_logged(login_page):
    login_page.navigate("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.login("Admin", "admin123")
    time.sleep(3) 
    assert "OrangeHRM" in login_page.page.title()
    yield login_page

