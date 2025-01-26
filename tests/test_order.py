import pytest
from pages.order_page import OrderPage
import allure
from locators.main_page_locators import ORDER_BUTTON_TOP, ORDER_BUTTON_BOTTOM

order_button_locators = [ORDER_BUTTON_TOP, ORDER_BUTTON_BOTTOM]
user_data_list = [
    {
        "first_name": "Иван",
        "last_name": "Иванов",
        "address": "г. Москва, ул. Тверская, д. 2",
        "metro_station": "Сокольники",
        "phone_number": "89001234567",
        "date": "15.01.2025",
        "rent_period": "сутки",
        "comment": "Тестовый заказ 1"
    },
    {
        "first_name": "Петр",
        "last_name": "Петров",
        "address": "г. Москва, Невский пр-т, д. 28",
        "metro_station": "Черкизовская",
        "phone_number": "89998765432",
        "date": "15.01.2024",
        "rent_period": "двое суток",
        "comment": "Тестовый заказ 2"
    }
]

@allure.feature('Order')
@pytest.mark.parametrize("order_button_locator, user_data", [(button, data)
for button in order_button_locators
for data in user_data_list])
def test_create_order(main_page_setup, order_button_locator, user_data):
    main_page = main_page_setup
    order_page = OrderPage(main_page.driver)

    main_page.click_order_button(order_button_locator)

    order_page.fill_order_form(
        user_data["first_name"],
        user_data["last_name"],
        user_data["address"],
        user_data["metro_station"],
        user_data["phone_number"],
        user_data["date"],
        user_data["rent_period"],
        user_data["comment"]
    )

    assert order_page.is_order_confirmation_popup_displayed(), "Всплывающее окно не появилось"