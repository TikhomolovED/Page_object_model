
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object.home_page import HomePage, LocatorsHomePage


class TestRedirectToDzen:
    def test_redirect_to_dzen(self,driver):
        home_page = HomePage(driver)
        home_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        home_page.find_element_located(LocatorsHomePage.YA_ICON).click()
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.BUTTON_INSTALL_YABROWSER))
        current_url = driver.current_url
        assert 'https://dzen.ru/' in current_url

