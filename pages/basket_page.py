from . import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert "Your basket is empty" in self.get_element(*BasketPageLocators.BASKET_TEXT).text
