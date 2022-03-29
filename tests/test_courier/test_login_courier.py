import allure
from helpers import Assertions
from helpers import BaseCase


@allure.title('Авторизация с существующим login')
def test_success_login(api_client):
    data = {
        "login": "test",
        "password": "1234"
    }
    response = api_client.post('/api/v1/courier', data=data)
    Assertions.assert_status_code_response(response, 201)
    Assertions.assert_value_by_json(response, 'ok', True)

    response = api_client.post('/api/v1/courier/login', data=data)
    Assertions.assert_status_code_response(response, 200)
    BaseCase.get_json_value(response, 'id')


@allure.title('Авторизация с несуществующим login')
def test_login_with_non_existent_login(api_client):
    data = {
        "login": "non_exist_users",
        "password": "1234"
    }

    response = api_client.post('/api/v1/courier/login', data=data)
    Assertions.assert_status_code_response(response, 404)
    Assertions.assert_value_by_json(response, 'message', 'Учетная запись не найдена')