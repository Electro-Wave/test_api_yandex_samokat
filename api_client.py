import requests


class ApiClient:
    def __init__(self, url):
        self.url = url

    def get(self, path: str, headers: dict = None, data: dict = None, cookies: dict = None, ):
        response = requests.get(self.url + path, headers=headers, params=data, cookies=cookies)
        return response

    def post(self, path: str, headers: dict = None, data: dict = None, cookies: dict = None):
        response = requests.post(self.url + path, headers=headers, json=data, cookies=cookies)
        return response

    def delete(self, path: str, headers: dict = None, params: dict = None, cookies: dict = None):
        response = requests.delete(self.url + path, headers=headers, params=params, cookies=cookies)
        return response

    def put(self, path: str, headers: dict = None, data: dict = None, cookies: dict = None):
        response = requests.get(self.url + path, headers=headers, data=data, cookies=cookies)
        return response
