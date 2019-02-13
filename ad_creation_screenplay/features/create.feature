# Created by Effortis at 2/6/2019
Feature: Create Campaign
  As an ad creator
  I want to be able to create ad campaigns
  when I choose a campaign objective and follow through the flow

  Scenario Outline: Create Campaign - Positive
    Given Ad_Creator is logged in
    When she clicks on Create Ad button
    And she chooses 155367MK ad account
    And she chooses Effortis page
    And she creates a new <campaign_type> campaign
    And she chooses an existing audience
    And I choose an ad design of type <ad_type>
    And I click on Next button
    And I click on Next button
    And I click on Next button
    And I click on Publish now button
    Then The campaign is successfully published

    Examples: Campaign
    | campaign_type     | ad_type       |
    | POST_ENGAGEMENT   | Page Post Ad  |
    | POST_ENGAGEMENT   | Photo Ad      |
    | PAGE_LIKES        | Page Like Ad  |
    | LINK_CLICKS       | Carousel Ad   |
    | CONVERSIONS       | Link Ad       |
    | LEAD_GENERATION   | Lead Ad       |
    | VIDEO_VIEWS       | Video Ad      |

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
