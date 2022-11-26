# {
#             uuid: uuid(),
#             path: path,
#             method: method,
#             statusCode: responseStatus,
#             parameters: queryParameters,
#             body: body,
# }
import json
import os
import sys
import uuid
from urllib import parse

import requests


def cover(response):
    req = response.request

    query_parameters = __parse_url_args(req.url)
    u = parse.urlparse(req.url)
    result = {
        "uuid": str(uuid.uuid4()),
        "path": u.path,
        "method": req.method,
        "statusCode": f"{response.status_code}",
        "parameters": query_parameters,
        "body": req.body,
    }

    __save_result(result)

    return response


def create_build(server_url, data, token):
    res = requests.post(f"{server_url}/{token}/builds", files={"file": ""}, data=data)
    return res.json()['resultsPath']


def upload_results(results_url, root_folder=os.path.join(sys.path[0], 'reqover-results')):
    for path in os.listdir(root_folder):
        if not path.endswith(".json"):
            continue

        absolute_file_path = os.path.join(root_folder, path)
        print(path)
        with open(absolute_file_path, "r") as f:
            data = json.loads(f.read())
            requests.post(results_url, json=data)


def __parse_url_args(url):
    query = parse.parse_qs(parse.urlparse(url).query)
    results = []
    for k, v in query.items():
        if v:
            value = ','.join(v)
        else:
            value = v
        results.append({"name": k, "value": value})
    return results


def __save_result(result, path=None):
    root_dir = sys.path[0]
    results_dir = path
    if not results_dir:
        results_dir = os.path.join(root_dir, "reqover-results")
    is_exist = os.path.exists(results_dir)

    if not is_exist:
        os.makedirs(results_dir)

    suffix = result['uuid']
    file_name = f"{results_dir}/{suffix}-coverage.json"
    with open(file_name, 'w') as outfile:
        json.dump(result, outfile)
