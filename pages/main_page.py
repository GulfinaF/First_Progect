from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
from .basket_page import BasketPage

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_all_products_list(self):
        all_products_btn=self.browser.find_element(*MainPageLocators.ALL_PRODUCTS_BUTTON)
        all_products_btn.click()
    def add_to_basket_3_product_on_page_button(self):
        basket_button = self.browser.find_element(*MainPageLocators. ADD_TO_BASKET_BUTTON_3_PRODUCT_ON_PAGE)
        basket_button.click()
    def should_not_be_success_message(self):
        assert self.is_element_present(*MainPageLocators.SUCCESS_MESSAGE), \
           "Success message is not presented"
