from .locators import BasketPageLocators
from .locators import ProductPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    #проверяем, что нет товаров
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
           "Basket is not empty"
    #проверяем, что есть сообщение о пустой корзине
    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BACKET_MESSAGE), \
               "There is no message about empty basket"

    def add_to_basket(self):
        basket_button = self.browser.find_element(*BasketPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()
        go_to_basket_button = self.browser.find_element(*BasketPageLocators.GO_TO_BASKET_BUTTON_AFTER_SUCCESS_MESSAGE)
        go_to_basket_button.click()

    def delete_item_from_basket(self):
        sum_of_items_befor_delete = self.browser.find_elements(*BasketPageLocators.BASKET_ITEMS)
        first_delete_button = self.browser.find_element(*BasketPageLocators.DELETE_FIRST_ITEM_BUTTON)
        sum_of_items_after_delete = self.browser.find_elements(*BasketPageLocators.BASKET_ITEMS)
        assert (len(sum_of_items_befor_delete) - 1)==(sum_of_items_after_delete), "Item is not deleted"
