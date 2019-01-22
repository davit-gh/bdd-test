# Created by Effortis at 1/10/2019
Feature: Create New Audience
  As an ad creator
  I want to be able to create new audiences
  when I navigate to Audience tab

  Scenario: Create audience modal
    Given I am on Audience page
    When MY AUDIENCES is chosen
    When I click on Create Audiences button
    Then I should see Create Audience modal

  Scenario: Create audiences - Locations and Language
    Given Create Audience modal is opened
    When I fill in and choose 2 locations
    And I click on Exclude link
    And I fill in and choose 2 excluded locations
    And I fill in and choose 2 languages
    And I switch the 3 SPLIT buttons to on
    And I click on Create button
    Then I should see 8 new audiences with correct combinations

  Scenario: Create audiences - Age and Gender
    Given Create Audience modal is opened
    When I fill in and choose a location
    And I select age range
    And I select a gender
    And I switch the 2 SPLIT buttons to on
    And I click on Create button
    Then I should see audiences of correct combinations

  Scenario: Create audiences - Details Targeting
    Given Create Audience modal is opened
    When I fill in and choose a location
    And I fill in and choose 2 Demographics, Interests or Behaviours
    And I fill in and choose an excluded Demographics, Interests or Behaviours
    And I fill in and choose an narrow Demographics, Interests or Behaviours
    And I switch the SPLIT button next to Demographics, Interests or Behaviours field
    And I click on Create button
    Then I should see 2 audiences of correct combinations

  Scenario: Create audiences - Connections
    Given Create Audience modal is opened
    When I fill in and choose a location
    And I fill in and choose users in Users Connect To field
    And I fill in and choose users in Friends of users connected to field
    And I click on Create button
    Then I edit the created audience and check that the values are saved

  Scenario: Create an audience - Place into a folder
    Given Create Audience modal is opened
    When I fill in and choose a location
    And At least one folder is created
    And I choose a folder from FOLDERS drop-down
    And I click on Create button
    Then The new audience should be placed into that folder

  Scenario: Create an audience - Place into a folder
    Given Create Audience modal is opened
    When I fill in and choose a location
    And I add 2 tags in TAGS field
    Then I should see the 2 tags added to the new audience

  Scenario: Create an audience - an exhaustive case
    Given Create Audience modal is opened
    When I fill in at least 2 values in each input field
    And I click on all split switches
    And I click on Create button
    Then The create number of new audiences are created
