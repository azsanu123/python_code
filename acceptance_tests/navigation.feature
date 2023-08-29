Feature: Standings pages
  As a fan
  In order to check a team's performance
  I want to view stats on the NBA stats page

  Scenario: A user can navigate to the standings page
    Given I am on the nba stats page
    When I click "Standings" on the menu
    Then I should navigate to the overall Eastern Conference Standings page


#  Scenario Outline: Navigate stats HomePage menu
#    Given I am on the nba stats page
#    When I click an "<item>" on the menu
#    Then I should navigate to the correct page "<url>"
#    Examples:
#      | item    | url                          |
#      |Schedule | https://www.nba.com/schedule |
#      |Teams    | https://www.nba.com/teams    |
#      |Stats    | https://www.nba.com/stats    |
#      |Players  | https://www.nba.com/players  |


  Scenario: Average points per game of two teams
    Given I am on the players traditional page
    When I filter stats for "Golden State Warriors" and "Houston Rockets"
    Then I should see the correct stats displayed filtered by "GOLDEN STATE WARRIORS" and "VS HOUSTON ROCKETS"



  Scenario: Search from homepage
    Given I am on the nba stats page
    When I search with the value "Lebron James"
    Then I should navigate to the player page