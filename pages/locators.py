from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_PRICE_TEXT = (By.XPATH, "//header//div[contains(@class, 'basket-mini')]")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button[type = 'submit']")
    PRODUCT_PRICE_TEXT = (By.XPATH, "//div[contains(@class, 'product_main')]/p[1]")
    NAME_PRODUCT = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
    NAME_PRODUCT_ON_MESSAGE = (By.XPATH, "//div[@id = 'messages']//strong")