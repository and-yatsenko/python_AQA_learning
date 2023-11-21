from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_basket_is_empty_text(self):
        basket_is_empty_text = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_TEXT).text
        expected_text = "Your basket is empty. Continue shopping"
        assert basket_is_empty_text == expected_text, (f"Текст на странице = '{basket_is_empty_text}' отличается от "
                                                       f"ожидаемого = '{expected_text}'")

    def should_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Корзина не пустая"
