from playwright.sync_api import Page, expect, Locator
from pages.base_page import BasePage
from pages.registration_page import loaded


class LoginPage(BasePage):

    URL = "https://rahulnxttrendz.ccbp.tech/login"

    def __init__(self, page: Page):
        super().__init__(page)

        self.username_input: Locator = page.get_by_placeholder("Username")
        self.password_input: Locator = page.get_by_placeholder("Password")
        self.login_button: Locator = page.get_by_role("button", name="Login", exact=True)
        self.home_heading: Locator = page.locator("h1.home-heading")

    def open_login_page(self):
        self.open_url(self.URL)
        
    def verify_login_page_url(self):
        expect(self.page).to_have_url(self.URL)

    def verify_login_page_ui(self):
        expect(self.username_input).to_be_visible()
        expect(self.password_input).to_be_visible()
        expect(self.login_button).to_be_visible()
        
    def enter_username(self, username: str) -> None:
        self.username_input.fill(username)

    def enter_password(self, password: str) -> None:
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()
        expect(self.home_heading).to_have_text("Clothes That Get YOU Noticed")

    def login(self, username: str = None, password: str = None):
        username = username if username is not None else loaded["login"]["email"]
        password = password if password is not None else loaded["login"]["password"]
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()


        