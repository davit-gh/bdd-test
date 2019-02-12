# Created by Effortis at 2/6/2019
Feature: Create Campaign
  As an ad creator
  I want to be able to create ad campaigns
  when I choose a campaign objective and follow through the flow

  Scenario Outline: Create Campaign - Positive
    Given Ad_Creator is logged in
    When she clicks on Create Ad button
    And she chooses Sandbox Adzwedo ad account
    And I choose Adscook page
    And I fill in a new campaign name
    And I click on <campaign> box
    And I click on Next button
    And I choose an existing audience
    And I click on Next button
    And I choose an ad design of type <ad_type>
    And I click on Next button
    And I click on Next button
    And I click on Next button
    And I click on Publish now button
    Then The campaign is successfully published

    Examples: Campaign
    | campaign          | ad_type       |
    | Post Engagements  | Page Post Ad  |
    | Post Engagements  | Photo Ad      |
    | Page Likes        | Page Like Ad  |
    | Web Traffic       | Carousel Ad   |
    | Conversions       | Link Ad       |
    | Lead Generation   | Lead Ad       |
    | Video Views       | Video Ad      |

  Scenario: Create Campaign - Publish Later
    Given I am logged in
    When I click on Create Ad button
    And I choose Sandbox Adzwedo ad account
    And I choose Adscook page
    And I fill in a new campaign name
    And I click on Conversions box
    And I click on Next button
    And I choose an existing audience
    And I click on Next button
    And I choose an any ad design
    And I click on Next button
    And I click on Next button
    And I click on Next button
    And I click on Publish Later button
    Then The campaign is moved to Unpublished Ads

  Scenario: Create Campaign - No Audience Selected
    Given I am logged in
    When I click on Create Ad button
    And I choose Sandbox Adzwedo ad account
    And I choose Adscook page
    And I fill in a new campaign name
    And I click on Conversions box
    And I click on Next button
    And I click on Next button
    Then I see error notification

  Scenario: Create Campaign - No Ad Design Selected
    Given I am logged in
    When I click on Create Ad button
    And I choose Sandbox Adzwedo ad account
    And I choose Adscook page
    And I fill in a new campaign name
    And I click on Conversions box
    And I click on Next button
    And I choose an existing audience
    And I click on Next button
    And I click on Next button
    Then I see error notification
