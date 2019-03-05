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
    And she chooses an <ad_design_type> ad design
    And she clicks on Next button
    And she clicks on Next button
    And she clicks on Publish now button
    Then The campaign is successfully published

    Examples: Campaign
    | campaign_type     | ad_design_type  |
    | POST_ENGAGEMENT   | Page Post Ad    |
    | POST_ENGAGEMENT   | Photo Ad        |
    | PAGE_LIKES        | Page Like Ad    |
    | LINK_CLICKS       | Carousel Ad     |
    | CONVERSIONS       | Link Ad         |
    | LEAD_GENERATION   | Lead Ad         |
    | VIDEO_VIEWS       | Video Ad        |

  Scenario: Publish Later
    Given Ad_Creator is logged in
    When she clicks on Create Ad button
    And she chooses 155367MK ad account
    And she chooses Effortis page
    And she creates a new CONVERSIONS campaign
    And she chooses an existing audience
    And she chooses an Link Ad ad design
    And she clicks on Next button
    And she clicks on Next button
    And she clicks on Publish Later link
    Then The campaign is moved to Unpublished Ads

  Scenario: No Audience Selected
    Given Ad_Creator is logged in
    When she clicks on Create Ad button
    And she chooses 155367MK ad account
    And she chooses Effortis page
    And she creates a new CONVERSIONS campaign
    And she clicks on Next button
    Then she sees Field is required error notification

  Scenario: No Ad Design Selected
    Given Ad_Creator is logged in
    When she clicks on Create Ad button
    And she chooses 155367MK ad account
    And she chooses Effortis page
    And she creates a new POST_ENGAGEMENT campaign
    And she chooses an existing audience
    And she clicks on Next button
    Then she sees Field is required error notification

  Scenario: Create Adset Per Ad Design
    Given Ad_Creator is logged in
    When she clicks on Create Ad button
    And she chooses 155367MK ad account
    And she chooses Effortis page
    And she creates a new POST_ENGAGEMENT campaign
    And she chooses 2 existing audiences
    And she chooses 3 Photo Ad ad designs
    And she splits on 3 placement options
    And she chooses to create adset per ad design
    And she clicks on Next button
    Then 18 adsets should be available for publishing
