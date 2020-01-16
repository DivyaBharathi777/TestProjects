Feature: Octopus test POC

  @tag_me
  Scenario: Octopus About Page
    Given Initialize browser setup
    When Open About page "https://octopusinvestments.com/investor/about-us/our-people/"
    When Search for a person "Chloe Allan"
    Then Validate profile "Chloe Allan"
    When Sort by options
    Then Validate test run success


