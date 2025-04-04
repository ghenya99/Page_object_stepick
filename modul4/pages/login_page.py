from .base_page import BasePage
from .locators import LoginPageLocators



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTR_FORM), "Registration form is not presented"

    def  register_new_user(self, email, password):
        email_link = self.browser.find_element(*LoginPageLocators.EMAIL)
        email_link.send_keys(email)

        psw_link = self.browser.find_element(*LoginPageLocators.PASSWORD)
        psw_link.send_keys(password)

        psw_link2 = self.browser.find_element(*LoginPageLocators.PASSWORD2)
        psw_link2.send_keys(password)

        registr_button = self.browser.find_element(*LoginPageLocators.REDISTR_BUTTON)
        registr_button.click()