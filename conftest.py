import pytest
import requests

from utils.api_helpers import (
    BASE_URL,
    LOGIN_URL,
    DELETE_URL,
    REGISTER_URL,
    ADMIN_USERNAME,
    ADMIN_PASSWORD,
)

@pytest.fixture
def test_user():

    user_data = {
        "username": "test_user55333",
        "email": "test_user55333@test.com",
        "password": "TestPassword55333"
    }

    register_response = requests.post(
        BASE_URL + REGISTER_URL,
        json=user_data
    )

    print("REGISTER:")
    print(register_response.status_code)
    print(register_response.text)

    assert register_response.status_code == 200

#обработка исключений
    try:
        register_json = register_response.json()
    except Exception as e:
        pytest.fail(f"Invalid JSON: {e}")

    user_id = register_json["account"]["id"]

    yield user_data, user_id

    admin_login_response = requests.post(
        BASE_URL + LOGIN_URL,
        json={
            "username": ADMIN_USERNAME,
            "password": ADMIN_PASSWORD
        }
    )

    assert admin_login_response.status_code == 200

    admin_token = admin_login_response.json()["access_token"]

    headers = {
        "Authorization": f"Bearer {admin_token}"
    }

    delete_response = requests.delete(
        f"{BASE_URL}{DELETE_URL}/{user_id}",
        headers=headers
    )

    print("DELETE:")
    print(delete_response.status_code)
    print(delete_response.text)