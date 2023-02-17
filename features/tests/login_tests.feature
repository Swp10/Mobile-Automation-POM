Feature: Testing a login for an application


  Scenario: With valid credential, I should be able to login
    Given I am on Login page
    When I login to account with valid credential
    Then I shall land on account home page dashboard
