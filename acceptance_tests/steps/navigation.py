from behave import *
from selenium import webdriver

from acceptance_tests.page_models.home_page import HomePage
from acceptance_tests.page_models.traditional_player_page import TraditionalPlayerPage

use_step_matcher('re')

@given('I am on the nba stats page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    page = HomePage(context.browser)
    page.driver.get(page.url)
    context.browser.maximize_window()

@given('I am on the players traditional page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    page = TraditionalPlayerPage(context.browser)
    page.driver.get(page.url)
    context.browser.maximize_window()



