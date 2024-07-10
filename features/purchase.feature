Feature: Purchase a Product

  Background:
    Given I open the website
    And I am on the sign-up page

  Scenario: Basic purchase of a product
    Given I am at home
    When I select the first product
    And I add it to the cart
    And I go to the cart and pay
    Then a message successful is displayed
