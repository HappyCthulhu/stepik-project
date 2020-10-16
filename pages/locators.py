from selenium.webdriver.common.by import By


class BaseLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_LOGIN = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[value='Register']")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert')
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, '.page_inner #messages strong')
    PRODUCT_NAME_IN_PRODUCT_PAGE = (By.CSS_SELECTOR, '.col-sm-6 h1')
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, '#messages :nth-child(3) strong')
    PRICE_IN_PRODUCT_PAGE = (By.CSS_SELECTOR, '.col-sm-6 .price_color')


class BasketPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items .row')
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, '#content_inner p')
