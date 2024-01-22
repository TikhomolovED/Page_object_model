from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


#https://qa-scooter.praktikum-services.ru/
class LocatorsHomePage:

    WHAT_IS_THE_PRICE = [By.XPATH, '//div[@id="accordion__heading-0"]']
    WANTS_ANY_SCOOTERS_AT_ONCE = [By.XPATH, "//div[@id='accordion__heading-1']"]
    HOW_CALCULATE_TIME = [By.XPATH, "//div[@id='accordion__heading-2']"]
    IS_POSSIBLE_TODAY = [By.XPATH, "//div[@id='accordion__heading-3']"]
    EXTEND_THE_TIME = [By.XPATH, "//div[@id='accordion__heading-4']"]
    BRING_CHARGERS =[By.XPATH, "//div[@id='accordion__heading-5']"]
    IS_POSSIBLE_CANCEL_ORDER = [By.XPATH, "//div[@id='accordion__heading-6']"]
    LIVE_OUTSIDE_FROM_MCAD = [By.XPATH, "//div[@id='accordion__heading-7']"]

    #AN=ANSWER
    AN_WHAT_IS_THE_PRICE = [By.XPATH, "//div[@id='accordion__panel-0']/p"]
    AN_WANTS_ANY_SCOOTERS_AT_ONCE = [By.XPATH, "//div[@id='accordion__panel-1']/p"]
    AN_HOW_CALCULATE_TIME = [By.XPATH, "//div[@id='accordion__panel-2']/p"]
    AN_IS_POSSIBLE_TODAY = [By.XPATH, "//div[@id='accordion__panel-3']/p"]
    AN_EXTEND_THE_TIME = [By.XPATH, "//div[@id='accordion__panel-4']/p"]
    AN_BRING_CHARGERS = [By.XPATH, "//div[@id='accordion__panel-5']/p"]
    AN_IS_POSSIBLE_CANCEL_ORDER = [By.XPATH, "//div[@id='accordion__panel-6']/p"]
    AN_LIVE_OUTSIDE_FROM_MCAD = [By.XPATH, "//div[@id='accordion__panel-7']/p"]

    BUTTON_ORDER = [By.XPATH, "//button[@class='Button_Button__ra12g']"]
    SCOOTER_ICON = [By.XPATH, "//img[@alt ='Scooter']"]
    YA_ICON = [By.XPATH, "//img[@alt ='Yandex']"]

    BUTTON_INSTALL_YABROWSER = [By.XPATH, "//div[@class ='sc738cd3f']"]

class HomePage(BasePage):

    def get_text_from_opened_questions(self, locator):
        text = self.find_element_located(locator).text
        return text


