from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class LocatorsOrderPage:
    INPUT_NAME = [By.XPATH, "//input[@placeholder ='* Имя']"]
    INPUT_SECOND_NAME = [By.XPATH, "//input[@placeholder ='* Фамилия']"]
    INPUT_ADDRESS = [By.XPATH, "//input[@placeholder ='* Адрес: куда привезти заказ']"]
    INPUT_PHONE_NUMBER = [By.XPATH, "//input[@placeholder ='* Телефон: на него позвонит курьер']"]
    CHOICE_METRO_STATION = [By.XPATH, "//input[@class ='select-search__input']"]
    SOKOLNIKI_STATION = [By.XPATH, "//button[@value='4']"]
    KRASNOSELSKAYA_STATION = [By.XPATH, "//button[@value='5']"]
    BUTTON_NEXT = [By.XPATH, "//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']"]

    INPUT_WHEN_TO_BRING_SCOOTER = [By.XPATH, "//input[@placeholder ='* Когда привезти самокат']"]
    CHOICE_DATE_30_J = [By.XPATH, "//div[@class = 'react-datepicker__day react-datepicker__day--030']"]
    CHOICE_DATE_31_J = [By.XPATH, "//div[@class = 'react-datepicker__day react-datepicker__day--031']"]
    INPUT_RENTAL_PERIOD = [By.XPATH, "//div[@class = 'Dropdown-control']"]
    CHOICE_ONE_DAY = [By.XPATH, "//div[contains(text(),'сутки')]"]
    CHOICE_TWO_DAYS =[By.XPATH, "//div[contains(text(),'двое суток')]"]
    BLACK_CHECK_BOX = [By.XPATH, "//input[@id = 'black']"]
    GREY_CHECK_BOX = [By.XPATH, "//input[@id = 'grey']"]
    COMMENT_FRO_COURIER = [By.XPATH, "//input[@placeholder ='Комментарий для курьера']"]
    BUTTON_MAKE_ORDER = [By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[3]/button[2]"]
    TITLE_POPUP = [By.XPATH, "//div[@class = 'Order_ModalHeader__3FDaJ']"]

    BUTTON_YES_POPUP = [By.XPATH, "//button[contains(text(),'Да')]"]
    TITTLE_POPUP_ORDER_COMPLETE = [By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']"]




class OrderPage(BasePage):
    pass