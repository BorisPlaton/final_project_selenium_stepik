from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class BasketPageLocators:
    BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner p")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL_INPUT = (By.ID, "id_registration-email")
    REGISTER_PASSWORD_INPUT = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD_CONFIRM_INPUT = (By.ID, "id_registration-password2")
    REGISTER_SUBMIT_BUTTON = (By.NAME, "registration_submit")


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
