import requests

from utils.api_helpers import (
    BASE_URL,
    LOGIN_URL,
    assert_error,
)

def test_get_nonexistent_profile():

    admin_login = requests.post(
        BASE_URL + LOGIN_URL,
        json={
            "username": "admin",
            "password": "admin123"
        }
    )

    admin_token = admin_login.json()["access_token"]

    headers = {
        "Authorization": f"Bearer {admin_token}"
    }

    response = requests.get(
        f"{BASE_URL}/api/profiles/999999",
        headers=headers
    )

    print(response.status_code, response.text)

    assert_error(
        response,
        expected_status=404,
        expected_message="Profile not found"
    )