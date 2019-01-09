# Created by Effortis at 12/6/2018

Feature: Page Like Ad Creation Screen
  As an ad creator
  I want to open Page Like Ad creation screen
  So that I can create Page Like Ads

  Scenario: Open the Page Like Ad creation screen
    Given Ad Design creation popup is opened
    When I select an Ad Account from adaccount drop-down
    And I select a page
    And I click on pageLikeAd box
    And I click on Next button
    Then I should see pageLikeAdType creation screen

  Scenario: Create single image link ad
    Given I am on pageLikeAd creation screen
    When I fill in a sample text in Text field
    And I click on Single Image box
    And I upload an image
    And I click on Create button on pageLikeAdType popup
    Then I should see the newly created Page Like Ad design

  Scenario: Create single image link ad
    Given I am on pageLikeAd creation screen
    When I fill in a sample text in Text field
    And I click on plus icon next to Text field
    And I fill in sample text in the second field
    And I click on Single Image box
    And I upload an image
    And I click on Create button on pageLikeAdType popup
    Then I should see 2 newly created Page Like Ad designs

  Scenario: Create single video ad
    Given I am on pageLikeAd creation screen
    When I fill in a sample text in Text field
    And I click on Single Video box
    And I upload a video
    And I click on Create button on pageLikeAdType popup
    Then I should see the newly created Page Like Ad design

  Scenario: Create slideshow ad
    Given I am on pageLikeAd creation screen
    When I fill in a sample text in Text field
    And I click on Slideshow box
    And I upload images
    And I click on Create button on pageLikeAdType popup
    Then I should see the newly created Link Ad design