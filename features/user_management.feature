Feature: User Management

  Background:
    Given the API base URL is configured
    And the timeout is set to 10 seconds

  Scenario: Create a new user
    Given the user data:
      | username | John |
      | job    |QA|
    When I send a POST request to "/users" with the user data
    Then the response status code should be 201
    And the response should contain the created user data