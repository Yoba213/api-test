import requests

BASE_URL = "https://secby.ru"
LOGIN_URL = "/api/auth/login"
PROFILE_URL = "/api/profiles/me"
LIST_PROFILES_URL = "/api/profiles/"
CHANGE_PASSWORD_URL = "/api/auth/change-password"
DELETE_URL = "/api/profiles"
REGISTER_URL = "/api/auth/register"

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def login(username, password):

    response = requests.post(
        BASE_URL + LOGIN_URL,
        json={
            "username": username,
            "password": password
        }
    )

    return response


def get_headers(token):

    return {
        "Authorization": f"Bearer {token}"
    }


def get_admin_profile(headers):

    response = requests.get(
        BASE_URL + PROFILE_URL,
        headers=headers
    )

    return response

def assert_error(response, expected_status: int, expected_message: str = None):

    assert response.status_code == expected_status

    response_json = response.json()

    assert "detail" in response_json

    if expected_message is not None:
        assert response_json["detail"] == expected_message