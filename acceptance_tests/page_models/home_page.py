from acceptance_tests.locators.home_page import HomePageLocators
from acceptance_tests.page_models.base_page import BasePage


class HomePage(BasePage):
    @property
    def url(self):
        return super(HomePage, self).url+'/'

    @property
    def click(self):
        return self.driver.find_element(*HomePageLocators.standings_menu)
