import os

import pytest
import requests

from src.reqover import cover, upload_results, create_build

# BASE_URL = 'https://petstore.swagger.io'
BASE_URL = 'http://localhost:8080'


@pytest.mark.parametrize("id", [1, 2, 3, None])
def test_can_get_pet_by_id(id):
    requests.get(f"{BASE_URL}/v2/pet/{id}").json()


@pytest.mark.parametrize("status", ["available", "sold", "net", "sold, available"])
def test_can_get_pet_by_status(status):
    requests.get(f"{BASE_URL}/v2/pet/findByStatus", params={"status": status}).json()


@pytest.mark.parametrize("id", [10])
def test_can_delete_pet_by_id(id):
    requests.delete(f"{BASE_URL}/v2/pet/{id}")


def test_get_inventory():
    requests.get(f"{BASE_URL}/v2/store/inventory")


def test_can_delete_pet():
    requests.delete(f"{BASE_URL}/v2/pet/1")
