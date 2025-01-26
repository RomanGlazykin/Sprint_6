from selenium.webdriver.remote.webdriver import WebDriver
from locators.order_page_locators import *
from .base_page import BasePage
from selenium.webdriver.common.by import By

class OrderPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        # Локаторы для полей формы заказа
        self.first_name_field = FIRST_NAME_FIELD
        self.last_name_field = LAST_NAME_FIELD
        self.address_field = ADDRESS_FIELD
        self.metro_station_field = METRO_STATION_FIELD
        self.phone_number_field = PHONE_NUMBER_FIELD
        self.next_button = NEXT_BUTTON

        self.date_field = DATE_FIELD
        self.rent_period_field = RENT_PERIOD_FIELD

        self.scooter_color_field = SCOOTER_COLOR_FIELD
        self.comment_field = COMMENT_FIELD
        self.order_button = ORDER_BUTTON
        self.accept_order_button = ACCEPT_ORDER_BUTTON

        # Локатор для всплывающего окна
        self.order_confirmation_popup = ORDER_CONFIRMATION_POPUP

    def enter_first_name(self, first_name):
        self.fill_field(self.first_name_field, first_name)

    def enter_last_name(self, last_name):
        self.fill_field(self.last_name_field, last_name)

    def enter_address(self, address):
        self.fill_field(self.address_field, address)

    def enter_metro_station(self, metro_station):
        self.fill_field(self.metro_station_field, metro_station)
        self.click_element((By.XPATH, "//ul[@class='select-search__options']/li[@data-index='0']"))

    def enter_phone_number(self, phone_number):
        self.fill_field(self.phone_number_field, phone_number)

    def click_next_button(self):
        self.click_element(self.next_button)

    def enter_date(self, date):
        self.fill_field(self.date_field, date)
        self.click_element((By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[4]/div[7]"))

    def enter_rent_period(self, period):
        self.click_element(self.rent_period_field)
        self.click_element((By.XPATH, f"//div[@class='Dropdown-option' and text()='{period}']"))

    def choose_scooter_color(self):
        self.click_element(self.scooter_color_field)

    def enter_comment(self, comment):
        self.fill_field(self.comment_field, comment)

    def click_order_button(self):
        self.click_element(self.order_button)

    def click_accept_order_button(self):
        self.click_element(self.accept_order_button)

    def is_order_confirmation_popup_displayed(self):
        return self.is_element_visible(self.order_confirmation_popup)

    def fill_order_form(self, first_name, last_name, address, metro_station, phone_number, date, period, comment):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_address(address)
        self.enter_metro_station(metro_station)
        self.enter_phone_number(phone_number)
        self.click_next_button()
        self.enter_date(date)
        self.enter_rent_period(period)
        self.choose_scooter_color()
        self.enter_comment(comment)
        self.click_order_button()
        self.click_accept_order_button()