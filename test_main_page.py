from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(driver, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина


def test_guest_should_see_login_link(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(driver, link)
    page.open()
    page.should_be_login_link()


def test_link_is_correct(driver):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    page = LoginPage(driver, link)
    page.open()
    page.should_be_login_url()


def test_there_is_login_form(driver):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    page = LoginPage(driver, link)
    page.open()
    page.should_be_login_form()


def test_there_is_registration_form(driver):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    page = LoginPage(driver, link)
    page.open()
    page.should_be_register_form()
