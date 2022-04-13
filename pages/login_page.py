from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == self.url, "Should be a login url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Should be a login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Should be a register form"

    def register_new_user(self, email, password):
        self.get_element(*LoginPageLocators.REGISTER_EMAIL_INPUT).send_keys(email)
        self.get_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT).send_keys(password)
        self.get_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM_INPUT).send_keys(password)
        self.get_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON).click()
