import allure
import pytest
from helpers import Assertions
from helpers import get_string


@allure.title('Создание курьера со всеми валидными полями')
def test_create_courier(api_client):
    data = {
        "login": get_string(3),
        "password": "1234",
        "firstName": "saske"
    }
    response = api_client.post('/api/v1/courier', data=data)
    Assertions.assert_status_code_response(response, 201)
    Assertions.assert_value_by_json(response, 'ok', True)


@allure.title('Создание курьера без обязательного поля firstName')
def test_create_courier_without_required_field_first_name(api_client):
    data = {
        "login": get_string(4),
        "password": "1234"
    }

    response = api_client.post('/api/v1/courier', data=data)
    Assertions.assert_status_code_response(response, 201)
    Assertions.assert_value_by_json(response, 'ok', True)


@pytest.mark.parametrize('login', [get_string(2), get_string(3), get_string(9), get_string(10)])
@allure.title('Позитивная проверка граничных значений поля Login')
def test_positive_boundary_value_filed_login(api_client, login):
    data = {
        "login": login,
        "password": "1234",
        "firstName": "saske"
    }

    with allure.step(f'Вввожу в поле login символы длиной {len(login)}'):
        response = api_client.post('/api/v1/courier', data=data)
    Assertions.assert_status_code_response(response, 201)
    Assertions.assert_value_by_json(response, 'ok', True)


@pytest.mark.parametrize('first_name', [get_string(2), get_string(3), get_string(9), get_string(10)])
@allure.title('Позитивная проверка граничных значений поля firstName')
def test_positive_boundary_value_filed_first_name(api_client, first_name):
    data = {
        "login": "ninza",
        "password": "1234",
        "firstName": first_name
    }
    with allure.step(f'Ввожу в поле firstName символы длиной {len(first_name)}'):
        response = api_client.post('/api/v1/courier', data=data)
    Assertions.assert_status_code_response(response, 201)
    Assertions.assert_value_by_json(response, 'ok', True)


@pytest.mark.parametrize('login', [get_string(1), get_string(11)])
@allure.title('Негативная проверка граничных значений поля login')
def test_negative_boundary_value_filed_login(login, api_client):
    data = {
        "login": login,
        "password": "1234",
        "firstName": "test"
    }
    with allure.step(f'Ввожу в поле login символы длиной {len(login)}'):
        response = api_client.post('/api/v1/courier', data=data)
    Assertions.assert_status_code_response(response, 400)


@pytest.mark.parametrize('first_name', [get_string(1), get_string(11)])
@allure.title('Негативная проверка граничных значений поля firstName')
def test_negative_boundary_value_filed_first_name(first_name, api_client):
    data = {
        "login": get_string(5),
        "password": "1234",
        "firstName": first_name
    }
    with allure.step(f'Ввожу в поле login символы длиной {len(first_name)}'):
        response = api_client.post('/api/v1/courier', data=data)
    Assertions.assert_status_code_response(response, 400)


@pytest.mark.parametrize('login, password', [('', '1234'), (get_string(3), '')])
@allure.title('Создание курьера без логина или пароля')
def test_create_courier_without_login_or_password(login, password, api_client):
    data = {
        "login": login,
        "password": password,
        "firstName": "test"
    }

    response = api_client.post('/api/v1/courier', data=data)
    Assertions.assert_status_code_response(response, 400)
    Assertions.assert_value_by_json(response, 'message', 'Недостаточно данных для создания учетной записи')
