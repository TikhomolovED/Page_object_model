from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def go_to_site(self, url):
        return self.driver.get(url)

    def find_element_located(self, locator, time = 10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message = f'Element not found in {locator}')

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)