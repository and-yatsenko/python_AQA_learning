from .base_page import BasePage
from .locators import ProductPageLocators, MainPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_basket_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_TEXT).text
        basket_price = self.browser.find_element(*MainPageLocators.BASKET_PRICE_TEXT).text[14:19]
        assert product_price == basket_price, (
            f"Цена корзины = '{basket_price}' отличается от цены товара = '{product_price}' после добавления")

    def should_name_of_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        product_name_on_message = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_ON_MESSAGE).text
        assert product_name == product_name_on_message, (
            f"Название товара = '{product_name}' отличается от товара добавленного в корзину = '{product_name_on_message}' после добавления")
