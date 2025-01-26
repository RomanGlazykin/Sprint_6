from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import *

class OrderPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

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
        self.driver.find_element(*self.first_name_field).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.last_name_field).send_keys(last_name)

    def enter_address(self, address):
        self.driver.find_element(*self.address_field).send_keys(address)

    def enter_metro_station(self, metro_station):
        self.driver.find_element(*self.metro_station_field).send_keys(metro_station)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='select-search__options']/li[@data-index='0']"))).click()

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)

    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def enter_date(self, date):
        self.driver.find_element(*self.date_field).send_keys(date)
        self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[4]/div[7]").click()

    def enter_rent_period(self, period):
        self.driver.find_element(*self.rent_period_field).click()
        self.driver.find_element(By.XPATH, f"//div[@class='Dropdown-option' and text()='{period}']").click()

    def choose_scooter_color(self):
        self.driver.find_element(*self.scooter_color_field).click()

    def enter_comment(self, comment):
        self.driver.find_element(*self.comment_field).send_keys(comment)

    def click_order_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.order_button))
        self.driver.find_element(*self.order_button).click()

    def click_accept_order_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.accept_order_button))
        self.driver.find_element(*self.accept_order_button).click()

    def is_order_confirmation_popup_displayed(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.order_confirmation_popup))
        return self.driver.find_element(*self.order_confirmation_popup).is_displayed()

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