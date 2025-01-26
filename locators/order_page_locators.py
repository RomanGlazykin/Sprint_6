from selenium.webdriver.common.by import By

FIRST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
LAST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
METRO_STATION_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
PHONE_NUMBER_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
NEXT_BUTTON = (By.XPATH, "//*[@id='root']/div/div[2]/div[3]/button")

DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
RENT_PERIOD_FIELD = (By.XPATH, "//div[text()='* Срок аренды']")

SCOOTER_COLOR_FIELD = (By.XPATH, "//*[@id='black']")
COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
ORDER_BUTTON = (By.XPATH, "//*[@id='root']/div/div[2]/div[3]/button[2]")
ACCEPT_ORDER_BUTTON = (By.XPATH, "//*[@id='root']/div/div[2]/div[5]/div[2]/button[2]")

ORDER_CONFIRMATION_POPUP = (By.XPATH, "//*[@id='root']/div/div[2]/div[5]/div[2]/button")