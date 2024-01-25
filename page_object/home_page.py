
from page_object.base_page import BasePage


class HomePage(BasePage):

    def get_text_from_opened_questions(self, locator):
        text = self.find_element_located(locator).text
        return text


