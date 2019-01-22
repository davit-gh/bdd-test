# Created by Effortis at 1/22/2019
Feature: #Enter feature name here
  # Enter feature description here

  Scenario: Edit Location
    Given Audience edit modal is opened
    When I edit Locations field
    And I click on Save button
    Then The location is changed

  Scenario: Edit Languages
    Given Audience edit modal is opened
    When I edit Languages field
    And I click on Save button
    Then The language is changed

  Scenario: Edit Age and Gender
    Given Audience edit modal is opened
    When I edit Age and Gender fields
    And I click on Save button
    Then The age and gender is changed

  Scenario: Edit Detailed Targeting
    Given Audience edit modal is opened
    When I edit Detailed Targeting fields
    And I click on Save button
    Then The age and gender is changed

  Scenario: Edit Custom Audience
    Given Audience edit modal is opened
    When I edit Custom Audience fields
    And I click on Save button
    Then The custom audience change is saved

  Scenario: Edit Folders
    Given Audience edit modal is opened
    When I choose a new folder from Folders drop-down
    And I click on Save button
    Then The audience is moved to that folder

  Scenario: Edit Tags
    Given Audience edit modal is opened
    When I edit the Tag field
    And I click on Save button
    Then The tag is edited