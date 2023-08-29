from selenium.webdriver.common.by import By
"""
locators for traditional player page view
"""

class TraditionalPlayerPageLocators:
    advanced_filters = By.CSS_SELECTOR, "div.StatsAdvancedFiltersPanel_safToggle__Veos4 > button > span"
    all_teams_filters = By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[1]/div/div/div[5]/div[1]/section[2]/div/div[1]/label/div/select'
    opponent_teams_filters = By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[1]/div/div/div[5]/div[1]/section[2]/div/div[2]/label/div/select'
    golden_state_warriors = By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[1]/div/div/div[5]/div[1]/section[2]/div/div[1]/label/div/select/option[11]'
    vs_houston_rockets = By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[1]/div/div/div[5]/div[1]/section[2]/div/div[2]/label/div/select/option[12]'
    get_stats_btn = By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[1]/div/div/div[5]/div[2]/div/button[2]'
    filtered_teams = By.CSS_SELECTOR, 'div.SplitsPills_sp__GHtfm'
    stats_table = By.CSS_SELECTOR, 'div.Crom_base__f0niE'