from .pages.product_page import ProductPage


# Шаги:
#     1. Открываем страницу продукта по ссылке
#     2. Кликаем на кнопку "Добавить в корзину"
# Ожидаемый результат:
#     1. Сообщение о том, что товар добавлен в корзину.
#         Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
#     2. Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_basket_price()
    page.should_name_of_product()
