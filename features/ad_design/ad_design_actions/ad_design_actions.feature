Feature: Ad Design actions
  As an ad creator
  I want to be able to perform some actions
  when I hover over an existing ad design

  @actions.hover
  Scenario: Hover Over Ad Design
    Given I am on Ad Design page
    And At least one ad design is created
    When I hover over the ad design
    Then I should see 5 action icons

  @actions.duplicate
  Scenario: Duplicate Ad design
    Given I am on Ad Design page
    And At least one ad design is created
    When I hover over the ad design
    And I click on Duplicate icon
    Then Success notification is displayed
    And The ad design is duplicated

  @actions.move
  Scenario: Move Ad Design to a Folder - Negative
    Given I am on Ad Design page
    And At least one ad design is created
    When I hover over the ad design
    And I click on Move To Folder icon
#    TODO replace it, popups are rendered even if they are not opened
    And A new popup is displayed with id moveToModal
    Then The button with class move-btn is disabled

  @actions.move
  Scenario: Move Ad Design to a Folder - Positive
    Given I am on Ad Design page
    And At least one ad design is created
    And At least one folder is created
    When I hover over the ad design
    And I click on Move To Folder icon
    And I select a folder and click on Move
    Then The ad is moved into the folder

  @actions.edit
  Scenario: Edit Ad Design
    Given I am on Ad Design page
    And At least one ad design is created
    And At least one folder is created
    When I hover over the ad design
    And I click on Edit icon
#    TODO replace it, popups are rendered even if they are not opened
    And A new popup is displayed with id createAdDesignModal

  @actions.preview
  Scenario Outline: Ad Design Preview
    Given I am on Ad Design page
    When I hover over the ad design of type <type>
    And I click on Preview icon
#    TODO replace it, popups are rendered even if they are not opened
    And A new popup is displayed with id preview-modal
    And All the previews display properly

    Examples: Types
      | type         |
      | Page Like Ad |
      | Page Post Ad |
      | Link Ad      |
      | Lead Ad      |
      | Photo Ad     |
      | Video Ad     |

  @actions.delete
  Scenario: Delete Ad Design
    Given I am on Ad Design page
    And At least one ad design is created
    When I hover over the ad design
    And I click on Delete icon
    Then A new popup is displayed with id deleteSelectedModal
    And I click on Delete button on popup
    And The ad is deleted

  @actions.select
  Scenario: Select Ad Designs
    Given I am on Ad Design page
    And At least one ad design is created
    When I hover over the ad design
    And Click on Select button
    Then The ad designs are selected

  @actions.unselect
  Scenario: Unselect Multiple Ad Designs
    Given I am on Ad Design page
    And At least two ad designs are selected
    When I click on Unselect all link
    Then The ad designs are unselected

  @actions.move
  Scenario: Move Multiple Ad Designs to a Folder
    Given I am on Ad Design page
    And At least two ad designs are created
    And At least one folder is created
    When I click on Move to
    And Choose a folder
    Then The ad designs are moved to that folder