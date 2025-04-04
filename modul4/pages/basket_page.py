from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_message_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), \
            "Empty message is presented, but should not be"
        message = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text
        assert f"Your basket is empty" in message, \
            f"Empty basket message is incorrect: '{message}'"

    def should_not_be_items_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items is presented, but should not be"