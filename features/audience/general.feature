Feature: Audience General
  As an ad creator
  I want to be able to perform some actions
  when I hover over an existing audience

  @general.pagination
  Scenario: Check Pagination
    Given Audience page is paginated
    And I select 24 Audiences Per Page from the pagination drop-down
    Then Less than or equal to 24 audiences are displayed

  Scenario: Sort Audiences by Date From Oldest to Newest
    Given I am on Audience page
    And At least one audience is created
    When I select sort type Date - Oldest to Newest
    Then The audiences are sorted by ascending order of date

  Scenario: Sort Audiences by Date From Newest to Oldest
    Given I am on Audience page
    And At least one audience is created
    When I select sort type Date - Oldest to Newest
    When I select sort type Date - Newest to Oldest
    Then The audiences are sorted by descending order of date

  @general.create_folder
  Scenario: Create A Folder
    Given I am on Audience page
    When I click on Add Folder and fill in a name
    And I click Save icon
    Then I see the folder listed under All

  Scenario: Filter Audiences by Ad Account
    Given I am on Audience page
    When I select Sandbox Adzwedo Ad Account from drop-down
    Then I should see ad designs belonging to Sandbox Adzwedo account

  Scenario Outline: Filter ad designs by Date
    Given I am on Audience page
    When I enter a date range from <date1> to <date2> in Date picker drop-down
    Then I should see ad designs from <date1> to <date2> date range

    Examples: Dates
    | date1         | date2       |
    | 24/01/2019    | 24/01/2019  |

  Scenario: Filter Audiences by Tags
    Given I am on Audience page
    When I enter aaa tag in Tags input field
    Then I should see audiences containing aaa tag
