# Created by Effortis at 12/5/2018

Feature: Page Post Ad Creation Screen
  As an ad creator
  I want to open Page Post Ad creation screen
  So that I can create Page Post Ads

  Scenario: Open the Page Post Ad creation screen
    Given Ad Design creation popup is opened
    When I select an Ad Account from adaccount drop-down
    And I select a page
    And I click on pagePostAd box
    And I click on Next button
    Then I should see pagePostAdType creation screen

  Scenario: Create a page post ad when published posts exist
    Given I am on pagePostAd creation screen
    And Published posts exist
    When I select a post
    And I click on Create button on pagePostAdType popup
    Then I should see the newly created Page Post Ad design

#  Scenario: Negative case when published posts don't exist
#    Given I am on pagePostAd creation screen
#    When Published posts does not exist
#    And I click on Create button on pagePostAdType popup
#    Then I should see an error message

  Scenario: Create a page post ad - negative
    Given I am on pagePostAd creation screen
    When I click on Create button on pagePostAdType popup
    Then I should see a validation error Field is required