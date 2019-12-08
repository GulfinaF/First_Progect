from .locators import BasketPageLocators
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
