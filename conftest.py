import os
import pytest
from api_client import ApiClient
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('URL')


@pytest.fixture(scope='function')
def api_client():
    return ApiClient(url)
