Feature: Form submission

  Scenario: Submit a form with multiple fields
    Given I am on the form page
    When I fill in the form with the following details:
      | field         | value          |
      | first_name    | John           |
      | last_name     | Doe            |
      | email         | john.doe@test.com |
    Then the form should be submitted successfully
