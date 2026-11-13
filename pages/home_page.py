from playwright.sync_api import Page, Locator, expect
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.home_link: Locator = page.get_by_role("link", name="Home")
        self.products_link = page.get_by_role("link",name="Products",exact=True)
        self.cart_link: Locator = page.get_by_role("link", name="Cart")
        self.logout_button: Locator = page.get_by_role("button", name="Logout")
        self.home_heading = page.get_by_role("heading",name="Clothes That Get YOU Noticed")
        self.shop_now_button = page.get_by_role("button",name="Shop Now")
        self.description = page.get_by_text("Fashion is part of the daily air",exact=False)
        
    def verify_home_heading(self) -> None:
        self.verify_visible(self.home_heading)
    def verify_home_link(self) -> None:
        self.verify_visible(self.home_link)
    def verify_products_link(self) -> None:
        self.verify_visible(self.products_link)
    def verify_cart_link(self) -> None:
        self.verify_visible(self.cart_link)
    def verify_logout_button(self) -> None:
        self.verify_visible(self.logout_button)
    def verify_shop_now_button(self) -> None:
        self.verify_visible(self.shop_now_button)
    def verify_description(self) -> None:
        self.verify_visible(self.description)
    def click_home(self) -> None:
        self.home_link.click()

    def click_cart(self) -> None:
        self.cart_link.click()
    def click_logout(self) -> None:
        self.logout_button.click()
    def click_shop_now(self) -> None:
        self.shop_now_button.click()
    
    def click_products(self):
        self.products_link.click()
        expect(self.page).to_have_url("https://rahulnxttrendz.ccbp.tech/products")
    