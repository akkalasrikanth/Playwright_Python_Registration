from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.home_page import HomePage
from pages.cart_page import CartPage

URL = "https://rahulnxttrendz.ccbp.tech/products"


def test_products_page_ui(page):
    login_page = LoginPage(page)
    login_page.open_login_page()
    login_page.login("rahul", "rahul@2021")
    HomePage(page).click_products()
    products_page = ProductsPage(page)
    products_page.verify_products_page_url()
    products_page.verify_products_heading()
    products_page.verify_products_list()
    products_page.verify_product_items()
    products_page.verify_product_count()


def test_first_product_navigation(page):
    login_page = LoginPage(page)
    login_page.open_login_page()
    login_page.login("rahul", "rahul@2021")
    home_page = HomePage(page)
    home_page.click_products()
    products_page = ProductsPage(page)
    products_page.click_first_product()

    expect(page).to_have_url(
        "https://rahulnxttrendz.ccbp.tech/products/1001"
    )


def test_shop_now_adds_incremented_product_to_cart(page):
    login_page = LoginPage(page)
    login_page.open_login_page()
    login_page.login("rahul", "rahul@2021")

    home_page = HomePage(page)
    home_page.verify_home_heading()
    home_page.click_shop_now()
    expect(page).to_have_url(URL)

    products_page = ProductsPage(page)
    products_page.click_first_product()

    expect(page).to_have_url(
        "https://rahulnxttrendz.ccbp.tech/products/1001"
    )
    expect(page.get_by_role("heading", name="Hair Dryer")).to_be_visible()

    products_page.increment_quantity(clicks=3)
    products_page.verify_quantity(expected_quantity=4)
    products_page.add_to_cart()

    home_page.click_cart()
    cart_page = CartPage(page)
    cart_page.verify_cart_page()
    cart_page.verify_item("Hair Dryer", "Phillips")
    cart_page.verify_item_quantity("Hair Dryer", 4)
    cart_page.verify_order_total("Rs 3040/-")
