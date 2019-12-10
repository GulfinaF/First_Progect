from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a:nth-child(1)")
    ALL_PRODUCTS_BUTTON =  (By.CSS_SELECTOR, ".dropdown > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)")
    ADD_TO_BASKET_BUTTON_3_PRODUCT_ON_PAGE = (By.CSS_SELECTOR, "li.col-xs-6:nth-child(3) > article:nth-child(1) > div:nth-child(4) > form:nth-child(3) > button:nth-child(3)")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(1) > div:nth-child(2)")
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button:nth-child(7)")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-lg:nth-child(3)")
    PRODUCT_NAME_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(1) > div:nth-child(2) > strong:nth-child(1)")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6:nth-child(2) > h1:nth-child(1)")
    PRODUCT_PRICE_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(3) > div:nth-child(2) > p:nth-child(1) > strong:nth-child(1)")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color:nth-child(2)")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,"div.alert:nth-child(1)")
class BasketPageLocators():
    EMPTY_BACKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p:nth-child(1)")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    GO_TO_BASKET_BUTTON_AFTER_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "a.btn-info:nth-child(1)")
    DELETE_FIRST_ITEM_BUTTON = (By.CSS_SELECTOR, "div.basket-items:nth-child(6) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > a:nth-child(1)")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-lg:nth-child(3)")
