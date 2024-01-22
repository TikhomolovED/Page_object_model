
import pytest
from page_object.order_page import LocatorsOrderPage, OrderPage
from page_object.home_page import LocatorsHomePage


class TestScooterOrder:

    @pytest.mark.parametrize('metro_station, rental_time',
                             [
                            [LocatorsOrderPage.SOKOLNIKI_STATION, LocatorsOrderPage.CHOICE_ONE_DAY],
                             [LocatorsOrderPage.KRASNOSELSKAYA_STATION, LocatorsOrderPage.CHOICE_TWO_DAYS]
                             ])
    def test_scooter_order(self, driver, metro_station, rental_time):
        order_page = OrderPage(driver)
        order_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        order_page.find_element_located(LocatorsHomePage.BUTTON_ORDER).click()
        order_page.find_element_located(LocatorsOrderPage.INPUT_NAME).send_keys('Евгений')
        order_page.find_element_located(LocatorsOrderPage.INPUT_SECOND_NAME).send_keys('Яндексович')
        order_page.find_element_located(LocatorsOrderPage.INPUT_ADDRESS).send_keys('Какой-то адрес')
        order_page.find_element_located(LocatorsOrderPage.INPUT_PHONE_NUMBER).send_keys('55555555555')
        order_page.find_element_located(LocatorsOrderPage.CHOICE_METRO_STATION).click()
        order_page.find_element_located(metro_station).click()
        order_page.find_element_located(LocatorsOrderPage.BUTTON_NEXT).click()

        order_page.find_element_located(LocatorsOrderPage.INPUT_WHEN_TO_BRING_SCOOTER).click()
        order_page.find_element_located(LocatorsOrderPage.CHOICE_DATE_30_J).click()
        order_page.find_element_located(LocatorsOrderPage.INPUT_RENTAL_PERIOD).click()
        order_page.find_element_located(rental_time).click()
        order_page.find_element_located(LocatorsOrderPage.BLACK_CHECK_BOX).click()
        order_page.find_element_located(LocatorsOrderPage.COMMENT_FRO_COURIER).send_keys('123')
        order_page.find_element_located(LocatorsOrderPage.BUTTON_MAKE_ORDER).click()

        order_page.find_element_located(LocatorsOrderPage.BUTTON_YES_POPUP).click()

        text = order_page.find_element_located(LocatorsOrderPage.TITTLE_POPUP_ORDER_COMPLETE).text
        assert 'Заказ оформлен' in text






