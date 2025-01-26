import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.main_page import MainPage
import time

BASE_URL = "https://qa-scooter.praktikum-services.ru/"

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def main_page_setup(driver):
    driver.get(BASE_URL)
    time.sleep(1)
    # Прокручиваем страницу вниз

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    return MainPage(driver)