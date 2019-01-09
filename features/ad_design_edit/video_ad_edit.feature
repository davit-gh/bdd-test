# Created by Effortis at 1/9/2019
Feature: Video Ad Edit
  As an ad creator
  I want to open Video Ad edit screen
  So that I can edit Video Ads

  # To be sure that only ad types of a certain type are displayed
  # you can use Ad Types drop-down
  Scenario: Edit a Photo Ad Text
    Given I am on Ad Design page
    And At least one ad design of type Video Ad is created
    When I hover over the ad design
    And I click on Edit icon1
    And I edit the Text field
    And I click on Save button on videoAdType popup
    Then The Text should change to the new value

  Scenario: Edit a Photo Ad Image
    Given I am on Ad Design page
    And At least one ad design of type Photo Ad is created
    When I hover over the ad design
    And I click on Edit icon1
    And I upload a new Single Video
    And I click on Save button on videoAdType popup
    Then The thumbnail image should change to the new image