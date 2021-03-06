# Created by Effortis at 12/6/2018

Feature: Video Ad Creation Screen
  As an ad creator
  I want to open Video Ad creation screen
  So that I can create Video Ads

  Scenario: Open the Video Ad creation screen
    Given Ad Design creation popup is opened
    When I select Adzwedo Sandbox Ad Account from adaccount drop-down
    And I select Test page page
    And I click on videoAd box
    And I click on Next button
    Then I should see videoAdType creation screen

  Scenario: Create a video ad - positive
    Given I am on videoAd creation screen
    When I upload a video file
    And I click on Create button on videoAdType popup
    Then I should see 1 newly created Video Ad designs

  Scenario: Create a video ad - negative
    Given I am on videoAd creation screen
    When I click on Create button on videoAdType popup
    Then I should see a validation error Field is required