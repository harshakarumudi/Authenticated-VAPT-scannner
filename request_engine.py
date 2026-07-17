import requests
from config import BASE_URL, SESSION_COOKIE, ENDPOINT

headers = {"User-Agent": "Mozilla/5.0"}
cookies = {"session": SESSION_COOKIE}

def send_request(object_id):
    url = f"{BASE_URL}{ENDPOINT}"
    response = requests.get(url, headers=headers, cookies=cookies,
                            params={"id": object_id},
                            allow_redirects=False, timeout=10)
    return response.status_code, response.text


def send_request_raw(endpoint):
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url, headers=headers, cookies=cookies,
                            allow_redirects=False, timeout=10)
    return response.status_code, response.text