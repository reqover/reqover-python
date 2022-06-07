# {
#             uuid: uuid(),
#             path: path,
#             method: method,
#             statusCode: responseStatus,
#             parameters: queryParameters,
#             body: body,
#         }
import json
import os
import sys
import uuid
from urllib import parse


def parse_url_args(url):
    query = parse.parse_qs(parse.urlparse(url).query)
    results = []
    for k, v in query.items():
        if v:
            value = ','.join(v)
        else:
            value = v
        results.append({"name": k, "value": value})
    return results


def reqover(response):
    req = response.request

    query_parameters = parse_url_args(req.url)
    u = parse.urlparse(req.url)
    result = {
        "uuid": str(uuid.uuid4()),
        "path": u.path,
        "method": req.method,
        "statusCode": f"{response.status_code}",
        "parameters": query_parameters,
        "body": req.body,
    }

    save_result(result)

    return response


def save_result(result, path=None):
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
