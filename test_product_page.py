import pytest

from .pages.product_page import ProductPage


# Шаги:
#     1. Открываем страницу продукта по ссылке
#     2. Кликаем на кнопку "Добавить в корзину"
# Ожидаемый результат:
#     1. Сообщение о том, что товар добавлен в корзину.
#         Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
#     2. Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
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


# Шаги:
#     1. Открываем страницу товара
#     2. Добавляем товар в корзину
# Ожидаемый результат:
#     Нет сообщения об успехе is_not_element_present
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.success_message_is_not_present()


# Шаги:
#     1. Открываем страницу товара
# Ожидаемый результат:
#     Нет сообщения об успехе с помощью is_not_element_present
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.success_message_is_not_present()


# Шаги:
#     1. Открываем страницу товара
#     2. Добавляем товар в корзину
# Ожидаемый результат:
#     Нет сообщения об успехе с помощью is_disappeared
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.success_message_is_disappeared()
