import requests

from utils.api_helpers import (
    login,
    get_headers,
    get_admin_profile,
    assert_error,
)

BASE_URL = "https://secby.ru"

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"


def test_get_user_profile(test_user):

    user_data, user_id = test_user

    login_response = login(
        user_data["username"],
        user_data["password"]
    )

    token = login_response.json()["access_token"]

    headers = get_headers(token)

    response = requests.get(
        f"{BASE_URL}/api/profiles/{user_id}",
        headers=headers
    )

    print("USER PROFILE:")
    print(response.status_code)
    print(response.text)

    assert response.status_code == 200
    assert response.json()["profile"]["id"] == user_id


def test_user_cannot_access_admin_profile(test_user):

    user_data, _ = test_user

    login_response = login(
        user_data["username"],
        user_data["password"]
    )

    token = login_response.json()["access_token"]
    headers = get_headers(token)

    admin_login = login(
        ADMIN_USERNAME,
        ADMIN_PASSWORD
    )

    assert admin_login.status_code == 200

    admin_token = admin_login.json()["access_token"]
    admin_headers = get_headers(admin_token)

    admin_profile = get_admin_profile(admin_headers)
    admin_id = admin_profile.json()["profile"]["id"]

    response = requests.get(
        f"{BASE_URL}/api/profiles/{admin_id}",
        headers=headers
    )

    print("USER TRY ADMIN PROFILE:")
    print(response.status_code)
    print(response.text)

    assert_error(
        response,
        expected_status=403,
        expected_message="Permission denied"
    )


def test_admin_can_access_admin_profile():

    admin_login = login(
        ADMIN_USERNAME,
        ADMIN_PASSWORD
    )

    assert admin_login.status_code == 200

    admin_data = admin_login.json()

    admin_token = admin_data["access_token"]
    admin_id = admin_data["user"]["id"]

    headers = get_headers(admin_token)

    response = requests.get(
        f"{BASE_URL}/api/profiles/{admin_id}",
        headers=headers
    )

    print("ADMIN USE OWN PROFILE:")
    print(response.status_code)
    print(response.text)

    assert response.status_code == 200
    assert response.json()["profile"]["id"] == admin_id