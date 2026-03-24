import os
import requests
import pytest


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://api.example.com")


@pytest.fixture(scope="session")
def auth_token():
    return os.getenv("API_TOKEN", "replace-me")


@pytest.fixture()
def api_client(base_url, auth_token):
    session = requests.Session()
    session.headers.update(
        {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {auth_token}",
        }
    )

    class Client:
        def request(self, method, path, json=None, params=None):
            url = f"{base_url}{path}"
            return session.request(method=method, url=url, json=json, params=params, timeout=10)

    return Client()
