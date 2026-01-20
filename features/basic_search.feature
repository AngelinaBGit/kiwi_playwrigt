@basic_search
Feature: Basic search form

  Scenario Outline: T1 - One way flight search
    Given As a not logged user I navigate to homepage "https://www.kiwi.com/en/"
    When I select one-way trip type
    And I set departure airport to "<origin>"
    And I set arrival airport to "<destination>"
    And I set departure date to "<days>" days from today
    And I uncheck "Check accommodation with booking.com"
    And I click the search button
    Then I am redirected to the search results page

Examples:
  | origin | destination | days |
  | RTM    | MAD         | 7    |
  | VCE    | BCN         | 14   |
