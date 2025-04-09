from selenium.webdriver.remote.webdriver import WebDriver
from locators.main_page_locators import *
from .base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        # Локаторы для кнопок "Заказать"
        self.order_button_top = ORDER_BUTTON_TOP
        self.order_button_bottom = ORDER_BUTTON_BOTTOM

        # Локаторы для выпадающего списка "Вопросы о важном"
        self.dropdown_arrows = [DROPDOWN_ARROW_1, DROPDOWN_ARROW_2, DROPDOWN_ARROW_3, DROPDOWN_ARROW_4, DROPDOWN_ARROW_5, DROPDOWN_ARROW_6, DROPDOWN_ARROW_7, DROPDOWN_ARROW_8]
        self.dropdown_texts = [DROPDOWN_TEXT_1, DROPDOWN_TEXT_2, DROPDOWN_TEXT_3, DROPDOWN_TEXT_4, DROPDOWN_TEXT_5, DROPDOWN_TEXT_6, DROPDOWN_TEXT_7, DROPDOWN_TEXT_8]

        # Локаторы для логотипов
        self.scooter_logo = SCOOTER_LOGO
        self.yandex_logo = YANDEX_LOGO


    def click_order_button(self, button_locator):
        self.click_element(button_locator)

    def click_dropdown_arrow(self, index: int):
        self.click_element(self.dropdown_arrows[index])

    def get_dropdown_text(self, index: int):
        return self.get_text(self.dropdown_texts[index])

    def click_scooter_logo(self):
        self.click_element(self.scooter_logo)

    def click_yandex_logo(self):
        self.click_element(self.yandex_logo)

