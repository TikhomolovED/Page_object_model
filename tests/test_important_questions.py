from constants import Constants
from locators import LocatorsHomePage
from page_object.home_page import HomePage


class TestImoptantQuestions:
    def test_important_questions_bring_chargers(self,driver):
        home_page = HomePage(driver)
        home_page.go_to_site(Constants.URL)
        home_page.scroll_to_element(LocatorsHomePage.BRING_CHARGERS)
        home_page.find_element_located(LocatorsHomePage.BRING_CHARGERS).click()
        current_text = home_page.get_text_from_opened_questions(LocatorsHomePage.AN_BRING_CHARGERS)
        expected_text = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
        assert current_text == expected_text

    def test_important_questions_extend_time(self,driver):
        home_page = HomePage(driver)
        home_page.go_to_site(Constants.URL)
        home_page.scroll_to_element(LocatorsHomePage.EXTEND_THE_TIME)
        home_page.find_element_located(LocatorsHomePage.EXTEND_THE_TIME).click()
        current_text = home_page.get_text_from_opened_questions(LocatorsHomePage.AN_EXTEND_THE_TIME)
        expected_text = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
        assert current_text == expected_text

    def test_important_questions_how_calculate_time(self,driver):
        home_page = HomePage(driver)
        home_page.go_to_site(Constants.URL)
        home_page.scroll_to_element(LocatorsHomePage.HOW_CALCULATE_TIME)
        home_page.find_element_located(LocatorsHomePage.HOW_CALCULATE_TIME).click()
        current_text = home_page.get_text_from_opened_questions(LocatorsHomePage.AN_HOW_CALCULATE_TIME)
        expected_text = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
        assert current_text == expected_text

    def test_important_questions_price(self,driver):
        home_page = HomePage(driver)
        home_page.go_to_site(Constants.URL)
        home_page.scroll_to_element(LocatorsHomePage.WHAT_IS_THE_PRICE)
        home_page.find_element_located(LocatorsHomePage.WHAT_IS_THE_PRICE).click()
        current_text = home_page.get_text_from_opened_questions(LocatorsHomePage.AN_WHAT_IS_THE_PRICE)
        expected_text = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        assert current_text == expected_text

    def test_important_questions_is_possible_cancel_order(self,driver):
        home_page = HomePage(driver)
        home_page.go_to_site(Constants.URL)
        home_page.scroll_to_element(LocatorsHomePage.IS_POSSIBLE_CANCEL_ORDER)
        home_page.find_element_located(LocatorsHomePage.IS_POSSIBLE_CANCEL_ORDER).click()
        current_text = home_page.get_text_from_opened_questions(LocatorsHomePage.AN_IS_POSSIBLE_CANCEL_ORDER)
        expected_text = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
        assert current_text == expected_text

    def test_important_questions_is_possible_today(self,driver):
        home_page = HomePage(driver)
        home_page.go_to_site(Constants.URL)
        home_page.scroll_to_element(LocatorsHomePage.IS_POSSIBLE_TODAY)
        home_page.find_element_located(LocatorsHomePage.IS_POSSIBLE_TODAY).click()
        current_text = home_page.get_text_from_opened_questions(LocatorsHomePage.AN_IS_POSSIBLE_TODAY)
        expected_text = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
        assert current_text == expected_text

    def test_important_questions_live_outside_from_mcad(self,driver):
        home_page = HomePage(driver)
        home_page.go_to_site(Constants.URL)
        home_page.scroll_to_element(LocatorsHomePage.LIVE_OUTSIDE_FROM_MCAD)
        home_page.find_element_located(LocatorsHomePage.LIVE_OUTSIDE_FROM_MCAD).click()
        current_text = home_page.get_text_from_opened_questions(LocatorsHomePage.AN_LIVE_OUTSIDE_FROM_MCAD)
        expected_text = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
        assert current_text == expected_text

    def test_important_questions_any_scooters(self,driver):
        home_page = HomePage(driver)
        home_page.go_to_site(Constants.URL)
        home_page.scroll_to_element(LocatorsHomePage.WANTS_ANY_SCOOTERS_AT_ONCE)
        home_page.find_element_located(LocatorsHomePage.WANTS_ANY_SCOOTERS_AT_ONCE).click()
        current_text = home_page.get_text_from_opened_questions(LocatorsHomePage.AN_WANTS_ANY_SCOOTERS_AT_ONCE)
        expected_text = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
        assert current_text == expected_text