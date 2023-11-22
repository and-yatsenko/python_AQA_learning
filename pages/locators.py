from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGOUT_LINK = (By.CSS_SELECTOR, "#logout_link")
    BASKET_BUTTON = (By.XPATH, "//div[@class = 'page_inner']//a[contains(@href, 'basket')]")


class MainPageLocators:
    BASKET_PRICE_TEXT = (By.XPATH, "//header//div[contains(@class, 'basket-mini')]")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.XPATH, "//form[@id = 'register_form']//input[@type = 'email']")
    REGISTER_PASSWORD1 = (By.XPATH, "//form[@id = 'register_form']//input[@name = 'registration-password1']")
    REGISTER_PASSWORD2 = (By.XPATH, "//form[@id = 'register_form']//input[@name = 'registration-password2']")
    REGISTER_BUTTON = (By.XPATH, "//form[@id = 'register_form']//button[@name = 'registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button[type = 'submit']")
    PRODUCT_PRICE_TEXT = (By.XPATH, "//div[contains(@class, 'product_main')]/p[1]")
    NAME_PRODUCT = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id = 'messages']//strong")
    BASKET_PRICE_ON_MESSAGE = (By.XPATH, "//div[@id = 'messages']//p[contains(text(), 'basket total')]/strong")


class BasketPageLocators:
    BASKET_IS_EMPTY_TEXT = (By.XPATH, "//div[@id='content_inner']/p[contains(text(), 'Your basket is empty')]")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
