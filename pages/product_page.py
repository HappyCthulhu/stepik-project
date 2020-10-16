from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_form = self.driver.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_form.click()

    def product_is_in_the_basket(self):
        assert self.driver.find_element(*ProductPageLocators.SUCCESS_MESSAGE), 'Product is not in the basket'

    def product_is_right(self):
        assert self.driver.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text == self.driver.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_PRODUCT_PAGE).text, 'There is wrong product in the basket'

    def price_is_correct(self):
        assert self.driver.find_element(*ProductPageLocators.PRICE_IN_PRODUCT_PAGE).text == self.driver.find_element(
            *ProductPageLocators.PRICE_IN_MESSAGE).text, 'price is different'

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
