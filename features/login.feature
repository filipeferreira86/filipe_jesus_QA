Feature: login

  Scenario Outline: Allow to show  error message when field is blank
    Given that I am in the site "https://uat.ormuco.com/login"
    When I inform "teste@teste.com.br" in the field "id=username"
    And I inform "senha" in the field "id=password"
    And I clear the field <field_clean>
    And I click at the button "xpath=/html/body/div/div/div/div[1]/div/form/ng-form/div[3]/div[2]/button"
    Then the site should show the message <message> in the field "xpath=/html/body/div/div/div/div[1]/div/form/ng-form/div[3]/div[1]/div/div/span"
    Examples:
      |field_clean               | message                               |
      |"id=username"             |"The user or password is incorrect."   |
      |"id=password"             |"The user or password is incorrect."   |

  Scenario: Allow to show  error message when field is blank
    Given that I am in the site "https://uat.ormuco.com/login"
    When I inform "teste@teste.com.br" in the field "id=username"
    And I inform "senha" in the field "id=password"
    And I click at the button "xpath=/html/body/div/div/div/div[1]/div/form/ng-form/div[3]/div[2]/button"
    Then the site should show the message "The user or password is incorrect." in the field "xpath=/html/body/div/div/div/div[1]/div/form/ng-form/div[3]/div[1]/div/div/span"
