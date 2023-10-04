# Created by francdelmonde at 10/3/23
Feature: verify that user is able to order Model 3 Vehicle

  Scenario: verify the order now button is clickable
    Given user navigate to homepage
    When user clicks on order now
    Then verify all model3 product components are present

  Scenario: user clicks on demo drive and verify the page opens to demo drive
    Given user navigate to homepage
    When user clicks on Tesla Model 3 Demo Drive
    Then Verify user is on Demo Drive page