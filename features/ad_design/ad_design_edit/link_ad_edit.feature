# Created by Effortis at 1/9/2019
Feature: Link Ad Edit
  As an ad creator
  I want to open Link Ad edit screen
  So that I can edit Link Ads

  # To be sure that only ad types of a certain type are displayed
  # you can use Ad Types drop-down
  Scenario: Edit a Link Ad Text
    Given I am on Ad Design page
    And At least one ad design of type Link Ad is created
    When I hover over the ad design
    And I click on Edit icon
    And I edit the postlink[0] field
    And I click on Save button on linkAdType popup
    Then The postlink[0] should change to the new value

  Scenario: Edit a Link Ad Image
    Given I am on Ad Design page
    And At least one ad design of type Link Ad is created
    When I hover over the ad design
    And I click on Edit icon
    And I upload a new Single Image
    And I click on Save button on linkAdType popup
    Then The thumbnail image should change to the new image

  Scenario: Edit a Link Ad Choose Video
    Given I am on Ad Design page
    And At least one ad design of type Link Ad is created
    When I hover over the ad design
    And I click on Edit icon
    And I choose a single video
    And I click on Save button on linkAdType popup
    Then The thumbnail image should change to the new image

  Scenario: Edit a Link Ad Upload Video
    Given I am on Ad Design page
    And At least one ad design of type Link Ad is created
    When I hover over the ad design
    And I click on Edit icon
    And I upload a single video
    And I click on Save button on linkAdType popup
    Then The thumbnail image should change to the new image