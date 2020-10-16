import time

from .locators import LoginPageLocators
from .base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес

        assert 'accounts/login/' in self.driver.current_url, \
            'wrong current url'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.driver.find_element(*LoginPageLocators.LOGIN_FORM), 'Login form is not present'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.driver.find_element(*LoginPageLocators.REGISTER_FORM), 'Register form is not present'

    def register_new_user(self, email, password):
        self.driver.find_element(*LoginPageLocators.REGISTER_LOGIN).send_keys(email)
        self.driver.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.driver.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD).send_keys(password)
        self.driver.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
