Feature: Carousel Ad Creation Screen
  As an ad creator
  I want to open Carousel Ad creation screen
  So that I can create Carousel Ads

  Scenario: User opens the Link Ad screen
    Given Ad Design creation popup is opened
    When I select Adzwedo Sandbox Ad Account from adaccount drop-down
    And I select Test page page
    And I click on carouselAd box
    And I click on Next button
    Then I should see carouselAdType creation screen

  @create.image_ad
  Scenario: Create image cards
    Given I am on carouselAd creation screen
    When I choose 1 image on each on of 3 cards
    And I fill in Destination URL field on each of 3 cards
    And I fill in See more URL: field
    And I click on Create button on carouselAdType popup
    Then I should see 1 newly created Carousel Ad designs

  @create.video_ad
  Scenario: Create video cards
    Given I am on carouselAd creation screen
    When I choose 1 video on each on of 3 cards
    And I fill in Destination URL field on each of 3 cards
    And I fill in See more URL: field
    And I click on Create button on carouselAdType popup
    Then I should see 1 newly created Carousel Ad designs

  @create.video_ad
  Scenario: Create slideshow cards
    Given I am on carouselAd creation screen
    When I choose 1 sildeshow on each on of 3 cards
    And I fill in Destination URL field on each of 3 cards
    And I fill in See more URL: field
    And I click on Create button on carouselAdType popup
    Then I should see 1 newly created Carousel Ad designs