# Created by Effortis at 1/11/2019
Feature: Audience actions
  As an ad creator
  I want to be able to perform some actions
  when I hover over an existing audience

  Scenario: Hover Over Audience
    Given I am on Audience page
    And At least one audience is created
    When I hover over the audience
    Then I should see 4 action icons

  Scenario: Select An Audience
    Given I am on Audience page
    And At least one audience is created
    When I hover over the audience
    And I click on Select button
    Then The audience is selected

  Scenario: Edit An Audience
    Given I am on Audience page
    And At least one audience is created
    When I hover over the audience
    And I click on Edit button
    Then Edit audience modal is opened

  Scenario: Edit An Audience
    Given I am on Audience page
    And At least one audience is created
    When I hover over the audience
    And I click on Edit button
    Then Edit audience modal is opened

  Scenario: Move An Audience To a Folder
    Given I am on Audience page
    And At least one audience is created
    And At least one folder is created
    When I hover over the audience
    And I click on Move button
    And I choose a folder and click on Move
    Then The audience is moved into that folder

  Scenario: Delete An Audience
    Given I am on Audience page
    And At least one audience is created
    When I hover over the audience
    And I click on Delete button
    And I click on Delete button on popup
    Then The audience is deleted