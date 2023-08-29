from acceptance_tests.locators.base_page import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'https://www.nba.com/stats'

    @property
    def title(self):
        return self.find_element(*BasePageLocators.TITLE)

    @property
    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    @property
    def search_field(self):
        return self.driver.find_element(*BasePageLocators.search_field)

    def search(self):
        text_box = self.search_field
        text_box.clear()
        text_box.send_keys()
