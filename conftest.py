
import pytest
from typing import Generator
from playwright.sync_api import Browser, BrowserContext, Page, Playwright
from pages.registration_page import RegistrationPage
from pathlib import Path


@pytest.fixture(scope="session")
def browser(playwright: Playwright) -> Generator[Browser, None, None]:
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture
def context(browser: Browser) -> Generator[BrowserContext, None, None]:
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture
def page(context: BrowserContext) -> Generator[Page, None, None]:
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture
def registration_page_fixture(page: Page) -> Generator[RegistrationPage, None, None]:
    registration = RegistrationPage(page)
    registration.open_registration_page()
    yield registration
    
folder = Path("reports")
folder.mkdir(exist_ok=True)

