import random
import time

import pytest

from .pages import ProductPageLocators, LoginPage, MainPage
from .pages.basket_page import BasketPage
from .pages import ProductPage


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(autouse=True, scope="function")
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        reg_page = LoginPage(browser, link)
        reg_page.open()
        reg_page.register_new_user(f"enedrink{str(time.time())}@email.com", "super_password")
        reg_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.is_not_element_present(*ProductPageLocators.FIRST_ALERT)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_add_to_cart_button()
        product_page.click_add_to_cart_button()
        product_page.check_alerts_after_adding_book()
        product_page.check_book_title_at_first_alert()
        product_page.check_book_price_at_third_alert()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_add_to_cart_button()
    product_page.click_add_to_cart_button()
    product_page.check_alerts_after_adding_book()
    product_page.check_book_title_at_first_alert()
    product_page.check_book_price_at_third_alert()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_add_to_cart_button()
    product_page.is_not_element_present(*ProductPageLocators.FIRST_ALERT)


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.is_not_element_present(*ProductPageLocators.FIRST_ALERT)


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_add_to_cart_button()
    product_page.is_disappeared(*ProductPageLocators.FIRST_ALERT)


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
