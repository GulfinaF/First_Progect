from pages.basket_page import BasketPage
import pytest
@pytest.mark.need_review_custom_scenarios
def test_guest_can_delete_product_from_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/visual-guide-to-lock-picking_206/"
    page = BasketPage(browser, link)
    page.open()
    page.add_to_basket()
    page.delete_item_from_basket()
