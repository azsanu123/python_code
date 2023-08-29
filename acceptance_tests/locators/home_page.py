from selenium.webdriver.common.by import By


class HomePageLocators():
    TITLE = By.TAG_NAME, 'h1'
    standings_menu = By.XPATH, '*//*[@id="nav-ul"]/li[8]/a/span'