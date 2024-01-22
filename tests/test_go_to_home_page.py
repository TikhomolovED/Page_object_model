from page_object.home_page import LocatorsHomePage
from page_object.order_page import OrderPage


class TestGoToHomePage:
    def test_go_to_home_page(self,driver):
        order_page = OrderPage(driver)
        order_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        order_page.find_element_located(LocatorsHomePage.BUTTON_ORDER).click()
        order_page.find_element_located(LocatorsHomePage.SCOOTER_ICON).click()
        current_url = driver.current_url
        assert current_url == 'https://qa-scooter.praktikum-services.ru/'




