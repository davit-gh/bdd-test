# Created by Effortis at 12/24/2018
Feature: Ad Design filtering
  As an ad creator
  I want to be able to select ad accounts/pages/ad types/date/tags
  So that I can view/create ad designs under that filters


  Scenario: Filter ad designs by Ad Account
    Given I am on Ad Design page
    When I select Sandbox Adzwedo Ad Account from drop-down
    Then That ad account is the selected option
    And I should see ad designs belonging to that account


  Scenario: Filter ad designs by Page
    Given I am on Ad Design page
    When I select Adscook Page from Pages drop-down
    Then That page is the selected option
    And I should see ad designs with pageid 223267218417113

  Scenario: Filter Pages
    Given I am on Ad Design page
    When I click on Pages drop-down
    Then I enter 3 letters in the page input box
    And I should see matching pages automatically filtered

  Scenario Outline: Filter ad designs by Ad Type
    Given I am on Ad Design page
    When I select an <ad_type> from Ad types drop-down
    Then I should see all the ad designs of <ad_type> ad type

    Examples: Ad Types
    | ad_type      |
    | Page Like Ad |
    | Link Ad      |
    | Lead Ad      |
    | Photo Ad     |
    | Video Ad     |

  Scenario Outline: Filter ad designs by Date
    Given I am on Ad Design page
    When I enter a date range from <date1> to <date2> in Date picker drop-down
    Then I should see ad designs from <date1> to <date2> date range

    Examples: Dates
    | date1         | date2       |
    | 30/12/2018    | 05/01/2019  |
    | 01/01/2017    | 04/01/2019  |
    | 01/12/2018    | 31/12/2018  |

  Scenario: Filter ad designs by Tags
    Given I am on Ad Design page
    When I enter tag1 tag in Tags input field
    Then I should see ad designs containing tag1 tag

  Scenario: Filter ad designs by Instagram applicable designs
    Given I am on Ad Design page
    When I click on Instagram icon
    Then I should see Instagram applicable ad designs