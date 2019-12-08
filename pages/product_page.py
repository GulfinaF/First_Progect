from .base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from .locators import ProductPageLocators
from .basket_page import BasketPage

class ProductPage(BasePage):
    def add_to_basket_button(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def should_be_add_to_basket_message(self):
        added_product_allert= self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE)
        product_name=self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert  product_name.text == added_product_allert.text , "This product didnt add to basket"

    def should_be_correct_price(self):
        added_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_SUCCESS_MESSAGE)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert  product_price.text == added_product_price.text , "Prices are different"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented"
