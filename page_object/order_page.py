

from constants import Constants
from locators import LocatorsOrderPage
from page_object.base_page import BasePage

class OrderPage(BasePage):

    def filling_form(self, metro_station, rental_time):
        self.find_element_located(LocatorsOrderPage.INPUT_NAME).send_keys(Constants.NAME)
        self.find_element_located(LocatorsOrderPage.INPUT_SECOND_NAME).send_keys(Constants.SECOND_NAME)
        self.find_element_located(LocatorsOrderPage.INPUT_ADDRESS).send_keys(Constants.ADDRESS)
        self.find_element_located(LocatorsOrderPage.INPUT_PHONE_NUMBER).send_keys(Constants.PHONE_NUMBER)
        self.find_element_located(LocatorsOrderPage.CHOICE_METRO_STATION).click()
        self.find_element_located(metro_station).click()
        self.find_element_located(LocatorsOrderPage.BUTTON_NEXT).click()

        self.find_element_located(LocatorsOrderPage.INPUT_WHEN_TO_BRING_SCOOTER).click()
        self.find_element_located(LocatorsOrderPage.CHOICE_DATE_30_J).click()
        self.find_element_located(LocatorsOrderPage.INPUT_RENTAL_PERIOD).click()
        self.find_element_located(rental_time).click()
        self.find_element_located(LocatorsOrderPage.BLACK_CHECK_BOX).click()
        self.find_element_located(LocatorsOrderPage.COMMENT_FRO_COURIER).send_keys(Constants.COMMENT_FOR_COURIER)
        self.find_element_located(LocatorsOrderPage.BUTTON_MAKE_ORDER).click()
