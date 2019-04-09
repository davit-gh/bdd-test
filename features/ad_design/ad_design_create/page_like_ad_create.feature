# Created by Effortis at 12/6/2018

Feature: Page Like Ad Creation Screen
  As an ad creator
  I want to open Page Like Ad creation screen
  So that I can create Page Like Ads

  Scenario: Open the Page Like Ad creation screen
    Given Ad Design creation popup is opened
    When I select Adzwedo Sandbox Ad Account from adaccount drop-down
    And I select Test page page
    And I click on pageLikeAd box
    And I click on Next button
    Then I should see pageLikeAdType creation screen

  Scenario: Create single image link ad
    Given I am on pageLikeAd creation screen
    When I edit the text[0] field
    And I click on Single Image box
    And I upload a single image for pageLikeAdType
    And I click on Create button on pageLikeAdType popup
    Then I should see 1 newly created Page Like Ad designs

  Scenario: Create single image link ad - Double Text
    Given I am on pageLikeAd creation screen
    When I edit the text[0] field
    And I click on plus button next to text[0] field
    And I edit the text[1] field
    And I upload a single image for pageLikeAdType
    And I click on Create button on pageLikeAdType popup
    Then I should see 2 newly created Page Like Ad designs

  Scenario: Create single video ad
    Given I am on pageLikeAd creation screen
    When I edit the Text field
    And I click on Single Video box
    And I upload a single video
    And I click on Create button on pageLikeAdType popup
    Then I should see 1 newly created Page Like Ad designs

  Scenario: Create slideshow ad
    Given I am on pageLikeAd creation screen
    When I edit the Text field
    And I click on Slideshow box
    And I upload multiple images as a slideshow
    And I click on Create button on pageLikeAdType popup
    Then I should see 1 newly created Page Like Ad designs