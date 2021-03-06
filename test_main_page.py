import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.locators import BasketPageLocators


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, driver):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(driver,
                        link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
        login_page = LoginPage(driver, driver.current_url)
        login_page.should_be_login_url()

    def test_guest_should_see_login_link(self, driver):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(driver, link)
        page.open()
        page.should_be_login_link()


def test_link_is_correct(driver):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    page = LoginPage(driver, link)
    page.open()
    page.should_be_login_page()


def test_there_is_login_form(driver):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    page = LoginPage(driver, link)
    page.open()
    page.should_be_login_form()


def test_there_is_registration_form(driver):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    page = LoginPage(driver, link)
    page.open()
    page.should_be_register_form()


def test_guest_cant_see_product_in_basket_opened_from_main_page(driver):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/'
    page = BasketPage(driver, link)
    page.open()
    page.go_to_basket_page()
    page.basket_is_empty(*BasketPageLocators.BASKET_ITEMS)
    page.empty_basket_text_is_present()
