Feature: DuckDuckGo API Search

  Scenario: Search for the term "Toledo" in DuckDuckGo API and verify response
    Given the duckduckgo API
    When I get to the API
    Then the response status is 200
    And the JSON response contain "Wikipedia" in the AbstractSource
    And by console the "FirstURL" and the "Text" of the records stored with "Name"
