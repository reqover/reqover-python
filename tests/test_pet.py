import json
import os
import sys

import pytest
import requests
from urllib import parse

import uuid as uuid

from src.reqover import reqover

BASE_URL = 'https://petstore.swagger.io'
# BASE_URL = 'http://localhost:3000/zscsguwimxhe/swagger'


@pytest.mark.parametrize("id", [1, 2, 3])
def test_can_get_pet_by_id(id):
    print(reqover(requests.get(f"{BASE_URL}/v2/pet/{id}")).json())


@pytest.mark.parametrize("status", ["available", "sold", "net", "sold, available"])
def test_can_get_pet_by_status(status):
    print(reqover(requests.get(f"{BASE_URL}/v2/pet/findByStatus", params={"status": status})).json())


@pytest.mark.parametrize("id", [10])
def test_can_delete_pet_by_id(id):
    reqover(requests.delete(f"{BASE_URL}/v2/pet/{id}"))
