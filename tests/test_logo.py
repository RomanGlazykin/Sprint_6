import time
import allure
from conftest import BASE_URL

@allure.feature('Logo')
def test_check_scooter_logo_redirect(main_page_setup):
    main_page = main_page_setup
    main_page.click_scooter_logo()
    assert main_page.driver.current_url == BASE_URL, "Редирект на главную страницу не произошел"

@allure.feature('Logo')
def test_check_yandex_logo_redirect(main_page_setup):
    main_page = main_page_setup
    main_page.click_yandex_logo()
    main_page.driver.switch_to.window(main_page.driver.window_handles[1])
    time.sleep(2)
    assert "dzen.ru" in main_page.driver.current_url, "Редирект на Дзен не произошел"
    main_page.driver.close()
    main_page.driver.switch_to.window(main_page.driver.window_handles[0])