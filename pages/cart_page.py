from playwright.sync_api import Locator, Page, expect

from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_heading: Locator = page.get_by_role("heading", name="My Cart")
        self.cart_items: Locator = page.get_by_role("listitem")
        self.order_total: Locator = page.get_by_role("heading").filter(
            has_text="Order Total:"
        )
        self.checkout_button: Locator = page.get_by_role(
            "button", name="Checkout"
        )

    def verify_cart_page(self) -> None:
        expect(self.page).to_have_url("https://rahulnxttrendz.ccbp.tech/cart")
        expect(self.cart_heading).to_be_visible()

    def get_item(self, product_name: str) -> Locator:
        return self.cart_items.filter(has_text=product_name)

    def verify_item(self, product_name: str, brand: str) -> None:
        item = self.get_item(product_name)
        expect(item).to_be_visible()
        expect(item).to_contain_text(brand)

    def verify_item_quantity(self, product_name: str, quantity: int) -> None:
        expect(
            self.get_item(product_name).get_by_text(str(quantity), exact=True)
        ).to_be_visible()

    def verify_order_total(self, expected_total: str) -> None:
        expect(self.order_total).to_contain_text(expected_total)