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
    Then verify that user sees Model 3

  Scenario: verify that user sees all components
    Given user navigate to homepage
    When scroll down the page to model 3
    And clicks on explore inventory
    And add zipcode 10977
    And user hover over model
    And user clicks on first product listed
    And store original window
    And switching to Tesla Model 3 product page
    Then verify all product components
    And close the Model 3 product page
    And switch back to the inventory page
    #title, picture, price, range, speed, vehicle details...
