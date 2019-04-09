# Created by Effortis at 12/6/2018

Feature: Lead Ad Creation Screen
  As an ad creator
  I want to open Lead Ad creation screen
  So that I can create Lead Ads

  Scenario: Open the Lead Ad creation screen
    Given Ad Design creation popup is opened
    When I select Adzwedo Sandbox Ad Account from adaccount drop-down
    And I select Test page page
    And I click on leadAd box
    And I click on Next button
    Then I should see leadAdType creation screen

  # To see a "Lead form" option choose "Effortis" page before
  # clicking on Lead Ad box
  Scenario: Create single image lead ad
    Given I am on leadAd creation screen
    When I upload a single image for leadAdType
    And I select an option from "Lead form" select box
    And I click on Create button on leadAdType popup
    Then I should see 1 newly created Lead Ad designs

  Scenario: Create single image lead ad - Double Text
    Given I am on leadAd creation screen
    When I edit the text[0] field
    And I click on plus button next to text[0] field
    And I edit the text[1] field
    And I upload a single image for leadAdType
    And I select an option from "Lead form" select box
    And I click on Create button on leadAdType popup
    Then I should see 2 newly created Lead Ad designs

  Scenario: Create single video ad
    Given I am on leadAd creation screen
    When I upload a single video
    And I select an option from "Lead form" select box
    And I click on Create button on leadAdType popup
    Then I should see 1 newly created Lead Ad designs

  Scenario: Create slideshow ad
    Given I am on leadAd creation screen
    When I upload multiple images as a slideshow
    And I select an option from "Lead form" select box
    And I click on Create button on leadAdType popup
    Then I should see 1 newly created Lead Ad designs

  Scenario: Create a lead ad - negative
    Given I am on leadAd creation screen
    When I click on Create button on leadAdType popup
    Then I should see a validation error Field is required