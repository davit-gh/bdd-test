# Created by Effortis at 12/5/2018

Feature: Link Ad Creation Screen
  As an ad creator
  I want to open Link Ad creation screen
  So that I can create Link Ads

  Scenario: User opens the Link Ad screen
    Given Ad Design creation popup is opened
    When I select an Ad Account from adaccount drop-down
    And I select a page
    And I click on linkAd box
    And I click on Next button
    Then I should see linkAdType creation screen

  Scenario: Create single image link ad
    Given I am on linkAd creation screen
    When Fill in the required post link address
    And I upload a single image
    And I click on Create button on linkAdType popup
    Then I should see the newly created Link Ad design

  Scenario: Create single image link ad
    Given I am on linkAd creation screen
    When I fill in the required post link URL
    And I click on plus button next to URL field
    And I fill in another URL
    And I fill in a headline text
    And I upload a single image
    And I click on Create button on linkAdType popup
    Then I should see 2 newly created Link Ad designs

  Scenario: Create single video ad
    Given I am on linkAd creation screen
    When I fill in the required post link URL
    And I upload a single video
    And I click on Create button on linkAdType popup
    Then I should see the newly created Link Ad design

  Scenario: Create slideshow ad
    Given I am on linkAd creation screen
    When I fill in the required post link URL
    And I upload multiple images as a slideshow
    And I click on Create button on linkAdType popup
    Then I should see the newly created Link Ad design

   Scenario: Create a link ad - negative
    Given I am on linkAd creation screen
    When I click on Create button on linkAdType popup
    Then I should see a validation error Field is required