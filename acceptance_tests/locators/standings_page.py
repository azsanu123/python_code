from selenium.webdriver.common.by import By

"""
locators for standings page stored here
"""

class StandingsPageLocators:
    eastern_conference = By.XPATH, '*//*[@id="__next"]/div[2]/div[2]/div[2]/section[2]/div'
    eastern_teams = By.XPATH, '*//*[@id="__next"]/div[2]/div[2]/div[2]/section[2]/div/div[2]/div[2]/table/tbody'