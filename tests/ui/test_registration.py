
import json
from pathlib import Path
from playwright.sync_api import expect
from pages.registration_page import RegistrationPage, loaded


class TestRegistrationPage:
    
    def test_open_registration_url(self, registration_page_fixture: RegistrationPage):
        registration_page_fixture.open_registration_page()

    def test_registration_page_url(self, registration_page_fixture: RegistrationPage):
        registration_page_fixture.verify_registration_page_url()
        
    def test_registration_register_user(self, registration_page_fixture: RegistrationPage):
        registration_page_fixture.register_user()
        
    def test_registration_login_page(self, registration_page_fixture: RegistrationPage):
        registration_page_fixture.register_user()
        registration_page_fixture.verify_registration_success()
        registration_page_fixture.click_login()
        
    def test_registration_page_ui(self, registration_page_fixture: RegistrationPage):
        registration_page_fixture.verify_registration_page_ui()
        
    def test_registration_page_title(self, registration_page_fixture: RegistrationPage):
        registration_page_fixture.verify_registration_page_title()
        
    def test_verify_json_data(self, registration_page_fixture: RegistrationPage):
        registration_page_fixture.register_user()
        
    def test_enter_name(self, registration_page_fixture: RegistrationPage):
        registration_page_fixture.enter_name(loaded["registration"]["name"])
        expect(registration_page_fixture.name_input).to_have_value(loaded["registration"]["name"])
        
    def test_enter_email(self, registration_page_fixture: RegistrationPage):
        registration_page_fixture.enter_email(loaded["registration"]["email"])
        expect(registration_page_fixture.email_input).to_have_value(loaded["registration"]["email"])
        
    def test_enter_password(self, registration_page_fixture: RegistrationPage):
        registration_page_fixture.enter_password(loaded["registration"]["password"])
        expect(registration_page_fixture.password_input).to_have_value(loaded["registration"]["password"])
        
    def test_select_gender(self, registration_page_fixture: RegistrationPage):
        registration_page_fixture.select_gender(loaded["registration"]["gender"][0])
        expect(registration_page_fixture.male_radio).to_be_checked()
        expect(registration_page_fixture.female_radio).not_to_be_checked()
        
    def test_country(self, registration_page_fixture: RegistrationPage):
        registration_page_fixture.select_country(loaded["registration"]["country"][2])
    
    def test_accept_terms(self, registration_page_fixture: RegistrationPage):
        registration_page_fixture.accept_terms()
        