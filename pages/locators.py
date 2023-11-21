from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.XPATH, "//div[@class = 'page_inner']//a[contains(@href, 'basket')]")
    # LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    BASKET_PRICE_TEXT = (By.XPATH, "//header//div[contains(@class, 'basket-mini')]")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button[type = 'submit']")
    PRODUCT_PRICE_TEXT = (By.XPATH, "//div[contains(@class, 'product_main')]/p[1]")
    NAME_PRODUCT = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id = 'messages']//strong")
    BASKET_PRICE_ON_MESSAGE = (By.XPATH, "//div[@id = 'messages']//p[contains(text(), 'basket total')]/strong")


class BasketPageLocators:
    BASKET_IS_EMPTY_TEXT = (By.XPATH, "//div[@id='content_inner']/p[contains(text(), 'Your basket is empty')]")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
