import allure
from helpers import Assertions


@allure.title('Удалить курера')
def test_delete_courier(api_client):
    response = api_client.delete('/api/v1/courier/1')
    Assertions.assert_status_code_response(response, 200)
    Assertions.assert_value_by_json(response, 'ok', True)


@allure.title('Удалить несуществующего курьера')
def test_delete_non_existent_courier(api_client):
    response = api_client.delete('/api/v1/courier/100')
    Assertions.assert_status_code_response(response, 404)
    Assertions.assert_value_by_json(response, 'message', 'Курьера с таким id нет.')


@allure.title('Удлаить курьера с пустым id')
def test_delete_courier_without_id(api_client):
    response = api_client.delete('/api/v1/courier/')
    Assertions.assert_status_code_response(response, 409)
    Assertions.assert_value_by_json(response, 'message', 'Недостаточно данных для удаления курьера')
