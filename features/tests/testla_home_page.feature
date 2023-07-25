Feature: verify all the elements on the home page are properly functioning

  Scenario: verify that user is able to set a demo drive
    Given user navigate to homepage
    When user clicks on demo drive
    Then user is taken to demo drive page

    Scenario: user is able to scroll down to  the model 3 and see its inventory
    Given user navigate to homepage
    When scroll down the page to model 3
    And clicks on explore inventory
    And add zipcode 10977
    Then verify that user sees to

    Scenario:  something
      Given user nagigates to https://www.tesla.com/inventory/new/m3
      When add zipcode 10977
      Then verify that user sees to


