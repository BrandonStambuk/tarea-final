import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
import time
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Cambia a True en CI
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
    login_page.navigate(BASE_URL)
    login_page.login(ADMIN_USERNAME, ADMIN_PASSWORD)
    time.sleep(3) 
    assert "OrangeHRM" in login_page.page.title()
    yield login_page

