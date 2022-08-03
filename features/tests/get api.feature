Feature: Verify get request on Zippopotam
  As a QA
  I want to run automated API tests for get requests
  so that we can confirm it is working correctly

Scenario: Verify get requests
  Given user hits get request
  When user receives the response
  Then the response should match