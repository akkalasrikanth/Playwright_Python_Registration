from playwright.sync_api import Page, expect, Locator

class BasePage:

    def __init__(self, page: Page):
        self.page = page
    
    def open_url(self, url: str) -> None:
        self.page.goto(url)
    
    def verify_url(self, expected_url: str) -> None:
        expect(self.page).to_have_url(expected_url)
    
    def verify_visible(self, locator: Locator) -> None:
        expect(locator).to_be_visible()