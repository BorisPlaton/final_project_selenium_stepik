from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    FIRST_ALERT = (By.CSS_SELECTOR, "div#messages div.alert:nth-child(1)")
    BOOK_TITLE_FIRST_ALERT = (By.CSS_SELECTOR, "div#messages div.alert:nth-child(1) strong")
    SECOND_ALERT = (By.CSS_SELECTOR, "div#messages div.alert:nth-child(2)")
    STRONG_TEXT_SECOND_ALERT = (By.CSS_SELECTOR, "div#messages div.alert:nth-child(2) strong")
    THIRD_ALERT = (By.CSS_SELECTOR, "div#messages div.alert:nth-child(3)")
    PRICE_THIRD_ALERT = (By.CSS_SELECTOR, "div#messages div.alert:nth-child(3) strong")
    BOOK_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

