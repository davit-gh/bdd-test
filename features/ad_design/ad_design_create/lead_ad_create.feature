# Created by Effortis at 12/6/2018

Feature: Lead Ad Creation Screen
  As an ad creator
  I want to open Lead Ad creation screen
  So that I can create Lead Ads

  Scenario: Open the Lead Ad creation screen
    Given Ad Design creation popup is opened
    When I select an Ad Account from adaccount drop-down
    And I select a page
    And I click on leadAd box
    And I click on Next button
    Then I should see leadAdType creation screen

  # To see a "Lead form" option choose "Effortis" page before
  # clicking on Lead Ad box
  Scenario: Create single image lead ad
    Given I am on leadAd creation screen
    And "Lead form" select box contains at least 1 option
    When I click on Single Image box
    And I upload an image
    And I select an option from "Lead form" select box
    And I click on Create button on leadAdType popup
    Then I should see the newly created Lead Ad design

  Scenario: Create single image lead ad
    Given I am on leadAd creation screen
    And "Lead form" select box contains at least 1 option
    When I edit the Text field
    And I click on plus icon next to Text field
    And I fill in sample text in the second field
    And I click on Single Image box
    And I upload an image
    And I select an option from "Lead form" select box
    And I click on Create button on leadAdType popup
    Then I should see 2 newly created Lead Ad designs

  Scenario: Create single video ad
    Given I am on leadAd creation screen
    When I click on Single Video box
    And I upload a single video
    And I select an option from "Lead form" select box
    And I click on Create button on leadAdType popup
    Then I should see the newly created Lead Ad design

  Scenario: Create slideshow ad
    Given I am on leadAd creation screen
    When I click on Slideshow box
    And I upload images
    And I select an option from "Lead form" select box
    And I click on Create button on leadAdType popup
    Then I should see the newly created Lead Ad design

  Scenario: Create a lead ad - negative
    Given I am on leadAd creation screen
    When I click on Create button on leadAdType popup
    Then I should see a validation error Field is required