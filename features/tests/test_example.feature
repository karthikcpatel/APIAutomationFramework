Feature: Search functionality

  Scenario Outline: Search for items
    Given I am on the Google search page
    When I search for "<search_term>"
    Then the title should contain "<expected_result>"

    Examples:
      | search_term | expected_result |
      | pytest      | pytest          |
      | selenium    | selenium        |
