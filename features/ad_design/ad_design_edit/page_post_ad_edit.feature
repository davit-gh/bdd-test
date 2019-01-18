# Created by Effortis at 1/9/2019
Feature: Page Post Ad Edit
  As an ad creator
  I want to open Psge Post Ad edit screen
  So that I can edit Psge Post Ads

  # To be sure that only ad types of a certain type are displayed
  # you can use Ad Types drop-down
  Scenario: Edit a Psge Post Ad Text
    Given I am on Ad Design page
    And At least one ad design of type Page Post Ad is created
    When I hover over the ad design
    And I click on Edit icon
    And I click on Select Published Page posts radio-button
    And I select a post
    And I click on Save button on pagePostAdType popup
    Then The thumbnail image should change to the new image

  Scenario: Edit a Psge Post Ad Image
    Given I am on Ad Design page
    And At least one ad design of type Psge Post Ad is created
    When I hover over the ad design
    And I click on Edit icon
    And I upload a new Single Image
    And I click on Save button on pagePostAdType popup
    Then The thumbnail image should change to the new image