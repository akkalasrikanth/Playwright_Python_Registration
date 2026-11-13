
from playwright.sync_api import expect

from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.products_page import ProductsPage

class TestRegistrationPage:

    def test_registration_page_url(self, registration_page_fixture: RegistrationPage):
        registration_page_fixture.verify_registration_page_title()
        registration_page_fixture.verify_registration_page_ui()
        registration_page_fixture.register_user()
        registration_page_fixture.click_login()
        login_page = LoginPage(registration_page_fixture.page)
        login_page.verify_login_page_url()
        login_page.verify_login_page_ui()
        login_page.login()
        home_page = HomePage(registration_page_fixture.page)
        home_page.click_products()
        product_page = ProductsPage(registration_page_fixture.page)
        product_page.add_product_cart()
        
        
       