from playwright.sync_api  import Page, Locator, expect
from pages.base_page import BasePage

class ProductsPage(BasePage):
    URL = "https://rahulnxttrendz.ccbp.tech/products"

    def __init__(self, page: Page):
        super().__init__(page)

        self.products_heading: Locator = page.get_by_role("heading", name="Exclusive Prime Deals")
        self.products_list: Locator = page.locator("ul.products-list").first
        self.product_items: Locator = page.locator("li.product-item")
        self.product_links: Locator = page.locator("a.link-item").first
        self.add_to_cart_button: Locator = page.get_by_role("button", name="ADD TO CART")
        self.increment_quantity_button: Locator = page.locator('button[testid="plus"]')
        self.quantity_display: Locator = page.locator("p.quantity")
        
    def add_product_cart(self):
        self.get_product_count()
        self.click_first_product()
        self.increment_quantity(clicks=3)
        self.verify_quantity(expected_quantity=4)
        self.add_to_cart()
        
        
        

    def verify_products_page_url(self):
        expect(self.page).to_have_url(self.URL)

    def verify_products_heading(self):
        expect(self.products_heading).to_have_text("Exclusive Prime Deals")

    def verify_products_list(self) -> None:
        expect(self.products_list).to_be_visible()

    def verify_product_items(self) -> None:
        expect(self.product_items).to_be_visible()

    def verify_product_count(self) -> None:
        assert self.product_items.count() > 0

    def click_first_product(self) -> None:
        self.product_links.click()

    def get_product_count(self) -> int:
        expect(self.product_items.first).to_be_visible()
        count = self.product_items.count()
        print(f"Total Products : {count}")
        return count
        

    def add_to_cart(self) -> None:
        expect(self.add_to_cart_button).to_be_visible()
        self.add_to_cart_button.click()

    def increment_quantity(self, clicks: int = 1) -> None:
        for _ in range(clicks):
            self.increment_quantity_button.click()

    def verify_quantity(self, expected_quantity: int) -> None:
        expect(self.quantity_display).to_have_text(str(expected_quantity))