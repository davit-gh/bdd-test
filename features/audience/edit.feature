# Created by Effortis at 1/22/2019
Feature: Edit Audience
  # Enter feature description here

  Scenario: Edit Location
    Given Edit Audience modal is opened
    When I edit Locations field and add 2 locations
    And I click on Save button on audience popup
    Then The location is changed

  Scenario: Edit Languages
    Given Edit Audience modal is opened
    When I edit Languages field
    And I click on Save button on audience popup
    Then The language is changed

  Scenario: Edit Age and Gender
    Given Edit Audience modal is opened
    When I edit Age and Gender fields
    And I click on Save button
    Then The age and gender is changed

  Scenario: Edit Detailed Targeting
    Given Edit Audience modal is opened
    When I edit Detailed Targeting fields
    And I click on Save button
    Then The age and gender is changed

  Scenario: Edit Custom Audience
    Given Edit Audience modal is opened
    When I edit Custom Audience fields
    And I click on Save button
    Then The custom audience change is saved

  Scenario: Edit Folders
    Given Edit Audience modal is opened
    When I choose a new folder from Folders drop-down
    And I click on Save button
    Then The audience is moved to that folder

  Scenario: Edit Tags
    Given Edit Audience modal is opened
    When I edit the Tag field
    And I click on Save button
    Then The tag is edited