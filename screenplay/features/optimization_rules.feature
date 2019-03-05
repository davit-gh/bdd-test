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
    And she clicks on rule_arrow js-edit-optim-rule icon on any rule
    And makes changes on the modal and clicks on Save button
    Then the changes are saved

  Scenario: Edit An Existing Rule - Negative
    Given Ad_Creator is on Optimization Rules page
    And at least 1 optimization rule is created
    And she clicks on rule_arrow js-edit-optim-rule icon on any rule
    And clicks on cancel_edit_btn button
    Then the modal is closed

  Scenario: Rule Assignment
    Given Ad_Creator is on Optimization Rules page
    And at least 1 optimization rule is created
    And she clicks on js-assign-rule icon on any rule
    And she searches for fin_Page Like campaign
    And chooses a campaign and clicks on Apply
    Then the rule is assigned to fin_Page Like campaign

  Scenario: Rule Assignment - Negative
    Given Ad_Creator is on Optimization Rules page
    And at least 1 optimization rule is created
    And she clicks on js-assign-rule icon on any rule
    And clicks on cancel_assign_btn button
    Then the modal is closed

  Scenario: Duplicate Rule
    Given Ad_Creator is on Optimization Rules page
    And at least 1 optimization rule is created
    And she clicks on dropdown icon on any rule
    And she clicks on Duplicate icon under that dropdown
    Then the rule is duplicated

  Scenario: Delete Rule
    Given Ad_Creator is on Optimization Rules page
    And at least 1 optimization rule is created
    And she clicks on dropdown icon on any rule
    And she clicks on Delete icon under that dropdown
    And she clicks on delete_rule_btn button
    Then the rule is deleted

  Scenario: Create Rule
    Given Ad_Creator is on Optimization Rules page
    And she clicks on create_rule_btn button
    And gives the rule name, adds conditions, chooses a schedule
    Then the rule is created