# Created by Effortis at 2/20/2019
Feature: Optimization Rules Automation
  As an ad create
  I want to be able to create and edit optimization rules
  when I navigate to Optimization Rules tab

  Scenario: Search For A Rule By Name
    Given Ad_Creator is on Optimization Rules page
    And at least 1 optimization rule is created
    And she searches for an existing rule titled name1
    Then the rules that are named name1 are filtered

  Scenario: Edit An Existing Rule
    Given Ad_Creator is on Optimization Rules page
    And at least 1 optimization rule is created
    And she clicks on Edit icon on any rule
    And makes changes on the modal and clicks on Save button
    Then the changes are saved

  Scenario: Edit An Existing Rule - Negative
    Given Ad_Creator is on Optimization Rules page
    And at least 1 optimization rule is created
    And she clicks on Edit icon on any rule
    And clicks on Cancel button
    Then the modal is closed

  Scenario: Rule Assignment
    Given Ad_Creator is on Optimization Rules page
    And at least 1 optimization rule is created
    And she clicks on Assign icon on any rule
    And she searches for a campaign by name
    And chooses a campaign and clicks on Apply
    Then the rule is assigned to that campaign

  Scenario: Rule Assignment - Negative
    Given Ad_Creator is on Optimization Rules page
    And at least 1 optimization rule is created
    And she clicks on Assign icon on any rule
    And clicks on Cancel button
    Then the modal is closed

  Scenario: Duplicate Rule
    Given Ad_Creator is on Optimization Rules page
    And at least 1 optimization rule is created
    And she clicks on Duplicate icon on any rule
    Then the rule is duplicated

  Scenario: Delete Rule
    Given Ad_Creator is on Optimization Rules page
    And at least 1 optimization rule is created
    And she clicks on Delete icon on any rule and confirms
    Then the rule is deleted

  Scenario: Create Rule
    Given Ad_Creator is on Optimization Rules page
    And she clicks on Create Rule button
    And gives the rule name, adds conditions, chooses a schedule
    And clicks on Save button
    Then the rule is created