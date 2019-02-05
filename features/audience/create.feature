# Created by Effortis at 1/10/2019
Feature: Create New Audience
  As an ad creator
  I want to be able to create new audiences
  when I navigate to Audience tab

  Scenario: Create audience modal
    Given I am on Audience page
    When I click on Create Audience button
    Then Edit/Create audience modal is opened

  Scenario: Create audiences - Locations and Language
    Given Create Audience modal is opened
    When I click on 1st Exclude link
    And I fill in and choose 1 locations
    And I fill in and choose 2 languages
    #And I switch the 3 SPLIT buttons to on
    And I click on Create button on audience popup
    Then I should see new audiences

  Scenario: Create audiences - Age and Gender
    Given Create Audience modal is opened
    When I click on 1st Exclude link
    And I fill in and choose 1 locations
    And I select age range
    And I select a gender
    #And I switch the 2 SPLIT buttons to on
    And I click on Create button on audience popup
    Then I should see new audiences

  Scenario: Create audiences - Details Targeting
    Given Create Audience modal is opened
    When I click on 1st Exclude link
    And I fill in and choose 1 locations
    And I click on 2nd Exclude link
    And I fill in and choose 2 Demographics, Interests or Behaviours
    And I fill in and choose an excluded Demographics, Interests or Behaviours
    And I fill in and choose an narrow Demographics, Interests or Behaviours
    #And I switch the SPLIT button next to Demographics, Interests or Behaviours field
    And I click on Create button on audience popup
    Then I should see new audiences

  Scenario: Create audiences - Connections
    Given Create Audience modal is opened
    When I click on 1st Exclude link
    And I fill in and choose 1 locations
    And I fill in and choose users in Users Connect To field
    And I fill in and choose users in Friends of users connected to field
    And I click on Create button on audience popup
#    TODO
    Then I should see new audiences

  Scenario: Create an audience - Place into a folder
    Given Create Audience modal is opened
    When I click on 1st Exclude link
    And I fill in and choose 1 locations
#    And At least one folder is created  TODO should be checked before opening modal window
    And I choose a folder from FOLDERS drop-down
    And I click on Create button on audience popup
    Then The audience is moved to that folder

  Scenario: Create an audience - Add multiple tags
    Given Create Audience modal is opened
    When I fill in and choose 1 locations
    And I add 2 tags in TAGS field
    Then I should see the 2 tags added to the new audience

  Scenario: Create an audience - an exhaustive case
    Given Create Audience modal is opened
    When I click on 1st Exclude link
    And I fill in and choose 2 locations
    And I fill in and choose 2 languages
    And I select age range
    And I select a gender
    And I click on 2nd Exclude link
    And I edit Detailed Targeting fields
    And I edit Connections fields
    And I click on 3nd Exclude link
    And I click on all split switches
    And I click on Create button on audience popup
    Then The correct number of new audiences are created
