import time

from selenium.webdriver.common.by import By


def test_presence_of_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(5)
    button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    assert button, "Кнопки на добавление в корзину нет"