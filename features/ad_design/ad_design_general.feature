# Created by Effortis at 12/24/2018
Feature: Ad Design General
  As an ad creator
  I want to see thumbnail images for the created ads
  when I navigate to the Ad Designs tab

  Scenario: Check thumbnail images
    Given I am on Ad Design page
    And The page contains ad designs of all 6 objectives
    Then I can see thumbnail images for all the ad designs

  @general.pagination
  Scenario: Check Pagination
    Given Ad Design page is paginated
    And I select 24 Ads Per Page from the pagination drop-down
    When I click on Next pagination link
    Then Less than or equal to 24 ad designs are displayed

  Scenario: Sort Ad Designs by Date From Oldest to Newest
    Given I am on Ad Design page
    And At least one ad design is created
    When I select sort type Date - Oldest to Newest
    Then The ad designs are sorted by ascending order of date

  Scenario: Sort Ad Designs by Date From Newest to Oldest
    Given I am on Ad Design page
    And At least one ad design is created
    When I select sort type Date - Oldest to Newest
    When I select sort type Date - Newest to Oldest
    Then The ad designs are sorted by descending order of date

  # click on Folders link on the left upper corner
  @general.create_folder
  Scenario: Create A Folder
    Given I am on Ad Design page
    When I click on Add Folder and fill in a name
    And I click Save icon
    Then I see the folder listed under All