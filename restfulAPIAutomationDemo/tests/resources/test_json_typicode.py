import requests
from pytest import mark
from tests.conftest import json_typicode_resource


@mark.json_typicode
class JsonTypicodeTests:
    def test_post_request_for_json_typicode(self, json_typicode_resource, body):
        response = requests.post(json_typicode_resource, json=body)
        assert response.status_code == 201
