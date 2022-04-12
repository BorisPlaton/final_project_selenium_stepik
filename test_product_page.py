from .pages import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_add_to_cart_button()
    product_page.click_add_to_cart_button()
    product_page.check_alerts_after_adding_book()
    product_page.check_book_title_at_first_alert()
    product_page.check_book_price_at_third_alert()
