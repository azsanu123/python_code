from behave import *
from selenium import webdriver

from acceptance_tests.locators.home_page import HomePageLocators
from acceptance_tests.locators.standings_page import StandingsPageLocators
from acceptance_tests.locators.traditional_player_page import TraditionalPlayerPageLocators
from acceptance_tests.page_models.home_page import HomePage
from acceptance_tests.page_models.traditional_player_page import TraditionalPlayerPage


@when('I click "Standings" on the menu')
def step_impl(context):
    context.browser.find_element(*HomePageLocators.standings_menu).click()
    eastern_conference = context.browser.find_element(*StandingsPageLocators.eastern_conference)
    eastern_conference.is_displayed()

@when('I click an "(.*)" on the menu')
def step_impl(context, item):
    menu = context.browser.find_element_by_link_text(item)
    menu.is_displayed()
    menu.click()

@when('I filter stats for "Golden State Warriors" and "Houston Rockets"')
def step_impl(context):
    page = TraditionalPlayerPage(context.browser)
    page.filter()

@when('When I search with the value "Lebron James""')
def step_impl(context):
    page = HomePage(context.browser)
    page.search()

