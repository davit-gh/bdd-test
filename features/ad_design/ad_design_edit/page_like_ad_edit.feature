# Created by Effortis at 1/9/2019
Feature: Page Like Ad Edit
  As an ad creator
  I want to open Page Like Ad edit screen
  So that I can edit Page Like Ads

  # To be sure that only ad types of a certain type are displayed
  # you can use Ad Types drop-down
  @edit.text
  Scenario: Edit a Page Like Ad Text
    Given I am on Ad Design page
    And At least one ad design of type Page Like Ad is created
    When I hover over the ad design of type Page Like Ad
    And I click on Edit icon
    And I edit the Text field
    And I click on Save button on pageLikeAdType popup
    Then The Text should change to the new value

  @edit.image
  Scenario: Edit a Lead Ad Image
    Given I am on Ad Design page
    And At least one ad design of type Page Like Ad is created
    When I hover over the ad design of type Page Like Ad
    And I click on Edit icon
    And I upload a new Single Image
    And I click on Save button on pageLikeAdType popup
    Then The thumbnail image should change to the new image

  Scenario: Edit a Lead Ad Image
    Given I am on Ad Design page
    And At least one ad design of type Link Ad is created
    When I hover over the ad design
    And I click on Edit icon
    And I add a new tag
    And I click on Save button on pageLikeAdType popup
    Then A new tag is added to that add design