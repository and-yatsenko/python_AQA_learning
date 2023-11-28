import time

import allure
import pytest

from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


@allure.description("""
Шаги:
    1. Открываем страницу продукта по ссылке
    2. Переходим на страницу логина
Ожидаемый результат:
    1. Есть кнопка логина
    2. Есть форма авторизации.""")
@pytest.mark.smoke
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"])
def test_guest_should_see_login_link_on_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@allure.description("""
Шаги:
    1. Открываем страницу продукта по ссылке
    2. Кликаем на кнопку "Добавить в корзину"
Ожидаемый результат:
    1. Сообщение о том, что товар добавлен в корзину.
        Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
    2. Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара. """)
@pytest.mark.regression
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
                                               "/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_basket_price()
    page.should_name_of_product()


@allure.description("""
Шаги:
    1. Открываем страницу товара
    2. Добавляем товар в корзину
Ожидаемый результат:
    Нет сообщения об успехе is_not_element_present """)
@pytest.mark.regression
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"])
def test_guest_cant_see_success_message_after_adding_product_to_basket_fail(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.success_message_is_not_present()


@allure.description("""
Шаги:
    1. Открываем страницу товара
Ожидаемый результат:
    Нет сообщения об успехе с помощью is_not_element_present """)
@pytest.mark.smoke
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.success_message_is_not_present()


@allure.description("""
Шаги:
    1. Открываем страницу товара
    2. Добавляем товар в корзину
Ожидаемый результат:
    Нет сообщения об успехе с помощью is_disappeared """)
@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.success_message_is_disappeared()


@allure.description("""
    Шаги:
        1. Открываем страницу по ссылке
        2. Переходим в корзину
    Ожидаемый результат:
        1. Корзина пустая
        2. Сообщение о том, что корзина пустая.""")
@pytest.mark.smoke
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_basket_is_empty()
    basket_page.should_basket_is_empty_text()


@pytest.mark.user
@pytest.mark.smoke
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        email = str(time.time())[:10] + "@fakemail.org"
        login_page.register_new_user(email, "uBwDHZCrXZcaqp6")
        login_page.should_be_authorized_user()
        yield
        login_page.logout()

    @allure.description("""
    Шаги:
        1. Открываем страницу продукта по ссылке
        2. Кликаем на кнопку "Добавить в корзину"
    Ожидаемый результат:
        1. Сообщение о том, что товар добавлен в корзину.
            Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
        2. Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.""")
    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"])
    def test_user_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_basket_price()
        page.should_name_of_product()

    @allure.description("""
    # Шаги:
    #     1. Открываем страницу товара
    # Ожидаемый результат:
    #     Нет сообщения об успехе с помощью is_not_element_present""")
    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"])
    def test_user_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.success_message_is_not_present()
