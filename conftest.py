import pytest
from playwright.sync_api import sync_playwright
# Cambia esta línea:
from pages.login_page import LoginPage
from pages.work_shifts_page import WorkShiftPage  # Nota: work_shifts_page (con 's')
import time


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
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
def work_shift_page(page):
    return WorkShiftPage(page)


@pytest.fixture(scope="function")
def page_logged(login_page):
    login_page.navigate("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.login("Admin", "admin123")
    time.sleep(3)
    assert "OrangeHRM" in login_page.page.title()
    yield login_page


@pytest.fixture(scope="function")
def work_shift_page_logged(work_shift_page, login_page):
    """Fixture que retorna WorkShiftPage ya autenticado y en el módulo correcto"""
    # Primero hacer login usando login_page
    login_page.navigate("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.login("Admin", "admin123")
    time.sleep(3)

    # Luego navegar al módulo Work Shift usando work_shift_page
    work_shift_page.navigate_to_work_shifts()
    time.sleep(2)

    yield work_shift_page