
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


class TestLoginPage:

    def test_success_page_login_navigation(self, registration_page_fixture: RegistrationPage):
        registration_page_fixture.register_user()
        registration_page_fixture.click_login()
        login_page = LoginPage(registration_page_fixture.page)
        login_page.verify_login_page_url()
        login_page.verify_login_page_ui()
        login_page.login()
        
