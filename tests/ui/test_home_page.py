from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.products_page import ProductsPage

def test_home_page_ui(page):
    registration_page = RegistrationPage(page)
    registration_page.open_registration_page()
    registration_page.register_user(
        "rahul",
        "rahul@example.com",
        "rahul@2021",
        "Male",
        "India"
    )
    registration_page.click_login()
    
    
    login_page = LoginPage(page)
    login_page.login("rahul", "rahul@2021")
    
    home_page = HomePage(page)
    home_page.verify_home_heading()
    home_page.verify_home_link()
    home_page.verify_products_link()
    home_page.verify_cart_link()
    home_page.verify_logout_button()
    home_page.verify_description()
    home_page.verify_shop_now_button()
    
def test_products_navigation(page):
    login_page = LoginPage(page)
    login_page.open_login_page()
    login_page.login("rahul", "rahul@2021")
    home_page = HomePage(page)
    home_page.click_products()
    ProductsPage(page).verify_products_page_url()
    