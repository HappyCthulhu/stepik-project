import math
from pages.locators import BaseLocators
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException


class BasePage:
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        # self.driver.implicitly_wait(timeout)

    def go_to_login_page(self):
        login_link = self.driver.find_element(*BaseLocators.LOGIN_LINK)
        login_link.click()
        # return LoginPage(driver=self.driver, url=self.driver.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*BaseLocators.LOGIN_LINK), "Login link is not presented"


    def open(self):
        self.driver.get(self.url)

    def solve_quiz_and_get_code(self):
        alert = self.driver.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
