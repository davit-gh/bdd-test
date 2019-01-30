# Created by Effortis at 1/22/2019
Feature: Edit Audience
  # Enter feature description here

  @edit.location
  Scenario: Edit Location
    Given Edit Audience modal is opened
    When I edit Locations field and add 2 locations
    And I click on Save button on audience popup
#    TODO
    Then The location is changed

  @edit.language
  Scenario: Edit Languages
    Given Edit Audience modal is opened
    When I edit Languages field
    And I click on Save button on audience popup
#    TODO
    Then The language is changed

  @edit.age_and_gender
  Scenario: Edit Age and Gender
    Given Edit Audience modal is opened
    When I edit Age and Gender fields
    And I click on Save button on audience popup
#    TODO
    Then The age and gender is changed

  @edit.targeting
  Scenario: Edit Detailed Targeting
    Given Edit Audience modal is opened
    When I edit Detailed Targeting fields
    And I click on Save button on audience popup
#    TODO
    Then The age and gender is changed

  @edit.audience
  Scenario: Edit Custom Audience
    Given Edit Audience modal is opened
    When I edit Custom Audience fields
    And I click on Save button on audience popup
#    TODO
    Then The custom audience change is saved

  @edit.folders
  Scenario: Edit Folders
    Given Edit Audience modal is opened
    When I choose a new folder from Folders drop-down
    And I click on Save button on audience popup
#  TODO
    Then The audience is moved to that folder

  @edit.tags
  Scenario: Edit Tags
    Given Edit Audience modal is opened
    When I Edit The Tags
    And I click on Save button on audience popup
#    TODO
    Then The tag is edited