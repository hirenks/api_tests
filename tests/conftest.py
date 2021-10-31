import pytest
import requests


@pytest.fixture
def get_json():
    def _response(url, path):
        json_response = requests.get(url + path)
        return json_response

    return _response
