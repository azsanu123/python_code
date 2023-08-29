from behave import *

from acceptance_tests.locators.standings_page import StandingsPageLocators
from acceptance_tests.page_models.traditional_player_page import TraditionalPlayerPage

use_step_matcher('re')

@then('I should navigate to the overall Eastern Conference Standings page')
def step_impl(context):
    eastern_conference_teams = context.browser.find_elements(*StandingsPageLocators.eastern_teams)
    assert isinstance(eastern_conference_teams, list)

@then('I should navigate to the correct page "(.*)"')
def step_impl(context, url):
    expected_url = url
    actual_url = context.browser.current_url
    assert expected_url == actual_url
    context.browser.quit()

@then('I should see the correct stats displayed filtered by "(.*)" and "(.*)"')
def step_impl(context, team_a, team_b):
    expected_team_a = team_a
    expected_team_b = team_b
    page = TraditionalPlayerPage(context.browser)
    actual_team_a = page.filtered_teams[0]
    actual_team_b = page.filtered_teams[1]
    assert actual_team_a.text == expected_team_a
    assert actual_team_b.text == expected_team_b

@then('I should navigate to the player page')
def step_impl(context):
    pass