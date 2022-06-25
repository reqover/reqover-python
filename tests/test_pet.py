import os

import pytest
import requests

from src.reqover import wrap, upload_results, create_build

BASE_URL = 'https://petstore.swagger.io'


# BASE_URL = 'http://localhost:3000/zscsguwimxhe/swagger'

@pytest.fixture(scope="session", autouse=True)
def setup():
    yield
    project_token = "ucg5jjvsftyn"
    data = {
        "name": os.getenv("BRANCH", "PR-1234"),
        "serviceUrl": "https://petstore.swagger.io",
        "swaggerUrl": "https://petstore.swagger.io/v2/swagger.json",
        "basePath": "/v2",
    }
    results_url = create_build("https://reqover-io.herokuapp.com", data, project_token)
    upload_results(results_url)


@pytest.mark.parametrize("id", [1, 2, 3, None])
def test_can_get_pet_by_id(id):
    print(wrap(requests.get(f"{BASE_URL}/v2/pet/{id}")).json())


@pytest.mark.parametrize("status", ["available", "sold", "net", "sold, available"])
def test_can_get_pet_by_status(status):
    print(wrap(requests.get(f"{BASE_URL}/v2/pet/findByStatus", params={"status": status})).json())


@pytest.mark.parametrize("id", [10])
def test_can_delete_pet_by_id(id):
    wrap(requests.delete(f"{BASE_URL}/v2/pet/{id}"))
