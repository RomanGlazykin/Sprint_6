from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator: tuple):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator: tuple):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_text(self, locator: tuple) -> str:
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def fill_field(self, locator: tuple, text: str):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def is_element_visible(self, locator: tuple) -> bool:
      try:
        return self.find_element(locator).is_displayed()
      except:
        return False