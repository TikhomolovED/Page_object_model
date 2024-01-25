
import pytest

from constants import Constants
from locators import LocatorsOrderPage, LocatorsHomePage
from page_object.order_page import OrderPage

class TestScooterOrder:

    @pytest.mark.parametrize('metro_station, rental_time',
                             [
                            [LocatorsOrderPage.SOKOLNIKI_STATION, LocatorsOrderPage.CHOICE_ONE_DAY],
                             [LocatorsOrderPage.KRASNOSELSKAYA_STATION, LocatorsOrderPage.CHOICE_TWO_DAYS]
                             ])
    def test_scooter_order(self, driver, metro_station, rental_time):
        order_page = OrderPage(driver)
        order_page.go_to_site(Constants.URL)
        order_page.find_element_located(LocatorsHomePage.BUTTON_ORDER).click()
        order_page.filling_form(metro_station, rental_time)

        order_page.find_element_located(LocatorsOrderPage.BUTTON_YES_POPUP).click()

        text = order_page.find_element_located(LocatorsOrderPage.TITTLE_POPUP_ORDER_COMPLETE).text
        assert 'Заказ оформлен' in text






