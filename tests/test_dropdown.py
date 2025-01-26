import allure

@allure.feature('Dropdown')
def test_check_dropdown_text_1(main_page_setup):
    main_page = main_page_setup

    main_page.click_dropdown_arrow_1()
    text = main_page.get_dropdown_text_1()

    expected_text = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    assert text == expected_text, f"Текст не совпадает. Ожидаемый: '{expected_text}', Фактический: '{text}'"

@allure.feature('Dropdown')
def test_check_dropdown_text_2(main_page_setup):
    main_page = main_page_setup

    main_page.click_dropdown_arrow_2()
    text = main_page.get_dropdown_text_2()

    expected_text = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    assert text == expected_text, f"Текст не совпадает. Ожидаемый: '{expected_text}', Фактический: '{text}'"

@allure.feature('Dropdown')
def test_check_dropdown_text_3(main_page_setup):
    main_page = main_page_setup

    main_page.click_dropdown_arrow_3()
    text = main_page.get_dropdown_text_3()

    expected_text = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    assert text == expected_text, f"Текст не совпадает. Ожидаемый: '{expected_text}', Фактический: '{text}'"

@allure.feature('Dropdown')
def test_check_dropdown_text_4(main_page_setup):
    main_page = main_page_setup

    main_page.click_dropdown_arrow_4()
    text = main_page.get_dropdown_text_4()

    expected_text = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    assert text == expected_text, f"Текст не совпадает. Ожидаемый: '{expected_text}', Фактический: '{text}'"

@allure.feature('Dropdown')
def test_check_dropdown_text_5(main_page_setup):
    main_page = main_page_setup

    main_page.click_dropdown_arrow_5()
    text = main_page.get_dropdown_text_5()

    expected_text = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    assert text == expected_text, f"Текст не совпадает. Ожидаемый: '{expected_text}', Фактический: '{text}'"

@allure.feature('Dropdown')
def test_check_dropdown_text_6(main_page_setup):
    main_page = main_page_setup

    main_page.click_dropdown_arrow_6()
    text = main_page.get_dropdown_text_6()

    expected_text = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    assert text == expected_text, f"Текст не совпадает. Ожидаемый: '{expected_text}', Фактический: '{text}'"

@allure.feature('Dropdown')
def test_check_dropdown_text_7(main_page_setup):
    main_page = main_page_setup

    main_page.click_dropdown_arrow_7()
    text = main_page.get_dropdown_text_7()

    expected_text = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    assert text == expected_text, f"Текст не совпадает. Ожидаемый: '{expected_text}', Фактический: '{text}'"

@allure.feature('Dropdown')
def test_check_dropdown_text_8(main_page_setup):
    main_page = main_page_setup

    main_page.click_dropdown_arrow_8()
    text = main_page.get_dropdown_text_8()

    expected_text = "Да, обязательно. Всем самокатов! И Москве, и Московской области."
    assert text == expected_text, f"Текст не совпадает. Ожидаемый: '{expected_text}', Фактический: '{text}'"
