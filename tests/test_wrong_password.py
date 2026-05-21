import requests

from utils.api_helpers import (
    BASE_URL,
    LOGIN_URL,
    assert_error,
)


def test_login_with_invalid_password(test_user):

    user_data, _ = test_user

    response = requests.post(
        BASE_URL + LOGIN_URL,
        json={
            "username": user_data["username"],
            "password": "WrongPassword123"
        }
    )

    print(response.status_code, response.text)

    assert_error(
        response,
        expected_status=401,
        expected_message="Incorrect username or password"
    )