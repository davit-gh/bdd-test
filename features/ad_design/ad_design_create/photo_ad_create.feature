# Created by Effortis at 12/6/2018

Feature: Photo Ad Creation Screen
  As an ad creator
  I want to open Photo Ad creation screen
  So that I can create Photo Ads

  Scenario: Open the Photo Ad creation screen
    Given Ad Design creation popup is opened
    When I select Adzwedo Sandbox Ad Account from adaccount drop-down
    And I select Test page page
    And I click on photoAd box
    And I click on Create button on photoAdType popup
    Then I should see photoAdType creation screen

  Scenario: Create a photo ad - positive
    Given I am on photoAd creation screen
    When I upload a single image for photoAdType
    And I click on Create button on photoAdType popup
    Then I should see 1 newly created Photo Ad designs

  Scenario: Create a photo ad - negative
    Given I am on photoAd creation screen
    When I click on Create button on photoAdType popup
    Then I should see a validation error Field is required