import pytest
from pages.order_page import OrderPage
import allure

@allure.feature('Order')
@pytest.mark.parametrize("order_button", ["top", "bottom"])
@pytest.mark.parametrize("user_data", [
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
])
def test_create_order(main_page_setup, order_button, user_data):
    main_page = main_page_setup
    order_page = OrderPage(main_page.driver)
    if order_button == "top":
        main_page.click_order_button_top()
    elif order_button == "bottom":
        main_page.click_order_button_bottom()
    order_page.enter_first_name(user_data["first_name"])
    order_page.enter_last_name(user_data["last_name"])
    order_page.enter_address(user_data["address"])
    order_page.enter_metro_station(user_data["metro_station"])
    order_page.enter_phone_number(user_data["phone_number"])
    order_page.click_next_button()
    order_page.enter_date(user_data["date"])
    order_page.enter_rent_period(user_data["rent_period"])
    order_page.choose_scooter_color()
    order_page.enter_comment(user_data["comment"])
    order_page.click_order_button()
    order_page.click_accept_order_button()
    assert order_page.is_order_confirmation_popup_displayed(), "Всплывающее окно не появилось"