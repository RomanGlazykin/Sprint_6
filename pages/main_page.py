from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import *

class MainPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

# Локаторы для кнопок "Заказать"
        self.order_button_top = ORDER_BUTTON_TOP
        self.order_button_bottom = ORDER_BUTTON_BOTTOM

# Локаторы для выпадающего списка "Вопросы о важном"
        self.dropdown_arrow_1 = DROPDOWN_ARROW_1
        self.dropdown_arrow_2 = DROPDOWN_ARROW_2
        self.dropdown_arrow_3 = DROPDOWN_ARROW_3
        self.dropdown_arrow_4 = DROPDOWN_ARROW_4
        self.dropdown_arrow_5 = DROPDOWN_ARROW_5
        self.dropdown_arrow_6 = DROPDOWN_ARROW_6
        self.dropdown_arrow_7 = DROPDOWN_ARROW_7
        self.dropdown_arrow_8 = DROPDOWN_ARROW_8

        self.dropdown_text_1 = DROPDOWN_TEXT_1
        self.dropdown_text_2 = DROPDOWN_TEXT_2
        self.dropdown_text_3 = DROPDOWN_TEXT_3
        self.dropdown_text_4 = DROPDOWN_TEXT_4
        self.dropdown_text_5 = DROPDOWN_TEXT_5
        self.dropdown_text_6 = DROPDOWN_TEXT_6
        self.dropdown_text_7 = DROPDOWN_TEXT_7
        self.dropdown_text_8 = DROPDOWN_TEXT_8

# Локаторы для логотипов
        self.scooter_logo = SCOOTER_LOGO
        self.yandex_logo = YANDEX_LOGO
#Нажатие на кнопки "Заказать"
    def click_order_button_top(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.order_button_top))
        self.driver.find_element(*self.order_button_top).click()

    def click_order_button_bottom(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.order_button_bottom))
        self.driver.find_element(*self.order_button_bottom).click()

#Нажатие на стрелки
    def click_dropdown_arrow_1(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.dropdown_arrow_1))
        self.driver.find_element(*self.dropdown_arrow_1).click()

    def click_dropdown_arrow_2(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.dropdown_arrow_2))
        self.driver.find_element(*self.dropdown_arrow_2).click()

    def click_dropdown_arrow_3(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.dropdown_arrow_3))
        self.driver.find_element(*self.dropdown_arrow_3).click()

    def click_dropdown_arrow_4(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.dropdown_arrow_4))
        self.driver.find_element(*self.dropdown_arrow_4).click()

    def click_dropdown_arrow_5(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.dropdown_arrow_5))
        self.driver.find_element(*self.dropdown_arrow_5).click()

    def click_dropdown_arrow_6(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.dropdown_arrow_6))
        self.driver.find_element(*self.dropdown_arrow_6).click()

    def click_dropdown_arrow_7(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.dropdown_arrow_7))
        self.driver.find_element(*self.dropdown_arrow_7).click()

    def click_dropdown_arrow_8(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.dropdown_arrow_8))
        self.driver.find_element(*self.dropdown_arrow_8).click()

#Нажатие на лого
    def click_scooter_logo(self):
            self.driver.find_element(*self.scooter_logo).click()

    def click_yandex_logo(self):
            self.driver.find_element(*self.yandex_logo).click()
#Получение текста
    def get_dropdown_text_1(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.dropdown_text_1))
        element = self.driver.find_element(*self.dropdown_text_1)
        return element.text

    def get_dropdown_text_2(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.dropdown_text_2))
        element = self.driver.find_element(*self.dropdown_text_2)
        return element.text

    def get_dropdown_text_3(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.dropdown_text_3))
        element = self.driver.find_element(*self.dropdown_text_3)
        return element.text

    def get_dropdown_text_4(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.dropdown_text_4))
        element = self.driver.find_element(*self.dropdown_text_4)
        return element.text

    def get_dropdown_text_5(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.dropdown_text_5))
        element = self.driver.find_element(*self.dropdown_text_5)
        return element.text

    def get_dropdown_text_6(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.dropdown_text_6))
        element = self.driver.find_element(*self.dropdown_text_6)
        return element.text

    def get_dropdown_text_7(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.dropdown_text_7))
        element = self.driver.find_element(*self.dropdown_text_7)
        return element.text

    def get_dropdown_text_8(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.dropdown_text_8))
        element = self.driver.find_element(*self.dropdown_text_8)
        return element.text

