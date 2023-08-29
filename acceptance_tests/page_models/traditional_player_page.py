from acceptance_tests.locators.traditional_player_page import TraditionalPlayerPageLocators
from acceptance_tests.page_models.base_page import BasePage


class TraditionalPlayerPage(BasePage):
    @property
    def url(self):
        return super(TraditionalPlayerPage, self).url + '/players/traditional'

    @property
    def advanced_filters(self):
        return self.driver.find_element(*TraditionalPlayerPageLocators.advanced_filters)

    @property
    def all_teams_filters(self):
        return self.driver.find_element(*TraditionalPlayerPageLocators.all_teams_filters)

    @property
    def select_golden_state_warriors(self):
        return self.driver.find_element(*TraditionalPlayerPageLocators.golden_state_warriors)

    @property
    def opponent_teams_filters(self):
        return self.driver.find_element(*TraditionalPlayerPageLocators.opponent_teams_filters)

    @property
    def select_vs_houston_rockets(self):
        return self.driver.find_element(*TraditionalPlayerPageLocators.vs_houston_rockets)

    @property
    def get_stats_btn(self):
        return self.driver.find_element(*TraditionalPlayerPageLocators.get_stats_btn)

    @property
    def get_stats_btn(self):
        return self.driver.find_element(*TraditionalPlayerPageLocators.stats_table)

    def filter(self):
        advanced_filters = self.advanced_filters
        advanced_filters.is_enabled()
        advanced_filters.click()
        all_teams_filters = self.all_teams_filters
        all_teams_filters.click()
        select_golden_state_warriors = self.select_golden_state_warriors
        select_golden_state_warriors.click()
        opponent_teams_filters = self.opponent_teams_filters
        opponent_teams_filters.click()
        select_vs_houston_rockets = self.select_vs_houston_rockets
        select_vs_houston_rockets.click()
        get_stats_btn = self.get_stats_btn()
        get_stats_btn.click()

    @property
    def filtered_teams(self):
        return self.driver.find_elements(*TraditionalPlayerPageLocators.filtered_teams)