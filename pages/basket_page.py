from pages.base_page import BasePage
from pages.locators import BaseLocators, BasketPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasketPage(BasePage):
    def basket_is_empty(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def empty_basket_text_is_present(self):
        text_empty_basket = self.driver.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT)
        assert 'Your basket is empty' in text_empty_basket.text, 'Wrong text im empty basket'
