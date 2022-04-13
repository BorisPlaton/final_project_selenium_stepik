import math

from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from . import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "No add to cart button"

    def click_add_to_cart_button(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def check_alerts_after_adding_book(self):
        assert self.is_element_present(*ProductPageLocators.FIRST_ALERT), "First alert isn't founded"
        assert self.is_element_present(*ProductPageLocators.SECOND_ALERT), "Second alert isn't founded"
        assert self.is_element_present(*ProductPageLocators.THIRD_ALERT), "Third alert isn't founded"

    def check_book_title_at_first_alert(self):
        assert self.get_element(*ProductPageLocators.BOOK_TITLE_FIRST_ALERT).text == self.get_element(
            *ProductPageLocators.BOOK_TITLE).text, "Book title isn't equal"

    def check_book_price_at_third_alert(self):
        assert self.get_element(*ProductPageLocators.PRICE_THIRD_ALERT).text == self.get_element(
            *ProductPageLocators.BOOK_PRICE).text, "Book price isn't equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.FIRST_ALERT), "Success message is presented, but should not be"
