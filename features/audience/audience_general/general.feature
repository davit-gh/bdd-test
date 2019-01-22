# Created by Effortis at 1/22/2019
Feature: #Enter feature name here
  # Enter feature description here

  @general.pagination
  Scenario: Check Pagination
    Given Audience page is paginated
    And I select 24 Audiences Per Page from the pagination drop-down
    When I click on Next pagination link
    Then Less than or equal to 24 audiences are displayed

  Scenario: Sort Ad Designs by Date From Oldest to Newest
    Given I am on Audiences page
    And At least one audience is created
    When I select sort type Date - Oldest to Newest
    Then The audiences are sorted by ascending order of date

  Scenario: Sort Audiences by Date From Newest to Oldest
    Given I am on Audiences page
    And At least one audience is created
    When I select sort type Date - Oldest to Newest
    When I select sort type Date - Newest to Oldest
    Then The audiences are sorted by descending order of date

  @general.create_folder
  Scenario: Create A Folder
    Given I am on Audiences page
    When I click on Add Folder and fill in a name
    And I click Save icon
    Then I see the folder listed under All

  Scenario: Filter Audiences by Ad Account
    Given I am on Audiences page
    When I select Sandbox Adzwedo Ad Account from drop-down
    Then That ad account is the selected option
    And I should see ad designs belonging to that account

  Scenario Outline: Filter ad designs by Date
    Given I am on Audiences page
    When I enter a date range from <date1> to <date2> in Date picker drop-down
    Then I should see ad designs from <date1> to <date2> date range

    Examples: Dates
    | date1         | date2       |
    | 30/12/2018    | 05/01/2019  |
    | 01/01/2017    | 04/01/2019  |
    | 01/12/2018    | 31/12/2018  |

  Scenario: Filter Audiences by Tags
    Given I am on Audiences page
    When I enter aaa tag in Tags input field
    Then I should see audiences containing aaa tag
