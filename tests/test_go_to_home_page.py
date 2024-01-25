from constants import Constants
from locators import LocatorsHomePage
from page_object.order_page import OrderPage


class TestGoToHomePage:
    def test_go_to_home_page(self,driver):
        order_page = OrderPage(driver)
        order_page.go_to_site(Constants.URL)
        order_page.find_element_located(LocatorsHomePage.BUTTON_ORDER).click()
        order_page.find_element_located(LocatorsHomePage.SCOOTER_ICON).click()
        current_url = driver.current_url
        assert current_url == Constants.URL




