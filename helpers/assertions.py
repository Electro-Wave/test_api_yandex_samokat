import allure
import curlify
import lxml.etree as ET
from json.decoder import JSONDecodeError
from requests import Response
from typing import Any


class Assertions:
    @staticmethod
    def assert_value_by_json(response: Response, name: str, expected_value: Any = None):
        try:
            response_as_dict = response.json()
        except JSONDecodeError as e:
            raise TypeError(e)

        assert name in response_as_dict, f'Cannot {name} in response'
        assert response_as_dict[
                   name] == expected_value, f'expected {expected_value}, response got {response_as_dict[name]}'

    @staticmethod
    def assert_status_code_response(response: Response, expected_code: int):
        try:
            assert response.status_code == expected_code
        except AssertionError:
            allure.attach(response.text, 'body_response', allure.attachment_type.TEXT)
            allure.attach(curlify.to_curl(response.request), 'CURL', allure.attachment_type.TEXT)
            raise AssertionError(f'expected status code {expected_code} got {response.status_code}')

    @staticmethod
    def assert_value_by_xml(response: Response, name: str, expected_name: Any):
        try:
            response_as_xml = ET.fromstring(response)
        except SyntaxError as e:
            allure.attach(response.text, 'bad response xml format',
                          allure.attachment_type.TEXT)
            raise AssertionError(e)
        res = ''
        for i in response_as_xml.iter(name):
            res = i.text
        assert res == expected_name, f'expected {expected_name} response got {res}'
