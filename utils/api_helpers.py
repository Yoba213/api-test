import requests

BASE_URL = "https://secby.ru"

LOGIN_URL = "/api/auth/login"
PROFILE_URL = "/api/profiles/me"


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