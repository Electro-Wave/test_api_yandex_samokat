from requests import Response
from json.encoder import JSONEncoder
from typing import Any


class BaseCase:
    @staticmethod
    def get_headers(response: Response, headers_name: str) -> Any:
        assert headers_name in response.headers, f'Cannot find headers'
        return response.headers[headers_name]

    @staticmethod
    def get_cookies(response: Response, cookie_name: str) -> Any:
        assert cookie_name in response.cookies, f'Cannot find cookie in cookies'
        return response.cookies[cookie_name]

    @staticmethod
    def get_json_value(response: Response, name: str) -> Any:

        try:
            response_as_dict = response.json()
        except JSONEncoder:
            raise AssertionError('response is no type json')
        assert name in response_as_dict, f'cannot find name in response'
        return response_as_dict[name]
