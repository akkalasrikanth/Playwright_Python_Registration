import json
from pathlib import Path
from playwright.sync_api import Page, expect, Locator 
from pages.base_page import BasePage

folder = Path("testData")
folder.mkdir(exist_ok=True)
data_file = folder / "registration.json"
loaded = json.loads(data_file.read_text(encoding="utf-8"))

class RegistrationPage(BasePage):

    URL = "https://rahulnxttrends.ccbp.tech/"

    def __init__(self, page: Page):
        super().__init__(page)
        self.registration_image: Locator = page.get_by_alt_text("Logo")
        self.registration_logo_image: Locator = page.get_by_alt_text("Registration Site Image")
        self.name_input: Locator = page.get_by_placeholder("Enter your name")
        self.email_input: Locator = page.get_by_placeholder("Enter your email")
        self.password_input: Locator = page.get_by_placeholder("Enter your password")
        self.male_radio = self.page.locator("input[type='radio']").nth(0)
        self.female_radio = self.page.locator("input[type='radio']").nth(1)
        self.country_dropdown: Locator = page.get_by_role("combobox", name="Country", exact=True)
        self.terms_checkbox: Locator = page.get_by_role("checkbox", name="I agree to the Terms & Conditions")
        self.register_button: Locator = page.get_by_role("button", name="Register",exact=True)
        self.already_account_text: Locator = page.locator("p.account-login").first
        self.login_link: Locator = page.get_by_role("link", name="Log in", exact=True)
        self.success_heading: Locator = page.get_by_role("heading", name="Registration Successful", exact=True)
        self.success_login_link: Locator = page.locator("#registrationSuccess a")
        self.continue_text: Locator = page.locator(
            "#registrationSuccess p.account-login"
        )
        
        self.gender_option = {
            "male": self.male_radio,
            "female": self.female_radio,
        }

    def open_registration_page(self):
        self.open_url(self.URL)

    def verify_registration_page_url(self):
        self.verify_url(self.URL)

    def verify_registration_page_title(self) -> None:
        expect(self.page).to_have_title("Registration Form")
        
    def register_user(self, name: str = None, email: str = None, password: str = None,
                     gender: str = None, country: str = None) -> None:
        name = name if name is not None else loaded["registration"]["name"]
        email = email if email is not None else loaded["registration"]["email"]
        password = password if password is not None else loaded["registration"]["password"]
        gender = gender if gender is not None else loaded["registration"]["gender"][0]
        country = country if country is not None else loaded["registration"]["country"][2]

        self.name_input.fill(name)
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.select_gender(gender)
        self.select_country(country)
        self.accept_terms()
        self.click_register()
        

    def verify_registration_page_ui(self) -> None:
            expect(self.registration_image).to_be_visible()
            expect(self.registration_logo_image).to_be_visible()
            
            expect(self.name_input).to_be_visible()
            expect(self.name_input).to_be_enabled()
            
            expect(self.email_input).to_be_visible()
            expect(self.email_input).to_be_enabled() 
            
            expect(self.password_input).to_be_visible()
            expect(self.password_input).to_be_enabled()
            
            expect(self.male_radio).to_be_visible()
            expect(self.female_radio).to_be_visible()
            
            expect(self.country_dropdown).to_be_visible()
            
            expect(self.terms_checkbox).to_be_visible()
            expect(self.terms_checkbox).not_to_be_checked()
            
            expect(self.register_button).to_be_visible()
            expect(self.register_button).to_be_enabled()
            expect(self.register_button).to_have_text("Register")
            expect(self.already_account_text).to_contain_text("Already have an account?")
            
            expect(self.login_link).to_be_visible()

    def enter_name(self, name: str) -> None:
            self.name_input.fill(name)

    def enter_email(self, email: str) -> None:
            self.email_input.fill(email)

    def enter_password(self, password: str) -> None:
            self.password_input.fill(password)

        
    def select_gender(self, gender: str) -> None:
        normalised_gender = gender.casefold()
        if normalised_gender not in self.gender_option:
            raise ValueError(f"Unsupported gender :{gender}")
        self.gender_option[normalised_gender].click()

    # Select country
    def select_country(self, country: str) -> None:
        self.country_dropdown.select_option(label=country)

    # Accept terms and conditions
    def accept_terms(self) -> None:
        self.terms_checkbox.check()
        expect(self.terms_checkbox).to_be_checked()

    # Click Register
    def click_register(self) -> None:
        self.register_button.click()
        expect(self.success_heading).to_contain_text("Registration Successful")

    # Verify successful registration
    def verify_registration_success(self) -> None:
        expect(self.success_heading).to_be_visible()
        expect(self.login_link).to_be_visible()

        
    def verify_registration_success_page(self) -> None:
        expect(self.success_heading).to_be_visible()
        expect(self.success_login_link).to_be_visible()
        expect(self.continue_text).to_be_visible()
        
    def click_login(self) -> None:
        self.success_login_link.click()
        expect(self.page).to_have_url("https://rahulnxttrendz.ccbp.tech/login"
)
