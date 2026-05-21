import requests

from utils.api_helpers import (
    BASE_URL,
    LOGIN_URL,
    ADMIN_PASSWORD,
    ADMIN_USERNAME,
    LIST_PROFILES_URL,
)

def test_admin_can_get_profiles_list():

    admin_login = requests.post(
        BASE_URL + LOGIN_URL,
        json={
            "username": ADMIN_USERNAME,
            "password": ADMIN_PASSWORD
        }
    )

    assert admin_login.status_code == 200

    admin_token = admin_login.json()["access_token"]

    headers = {
        "Authorization": f"Bearer {admin_token}"
    }

    response = requests.get(
        BASE_URL + LIST_PROFILES_URL,
        headers=headers
    )

    print("ADMIN PROFILES LIST:")
    print(response.status_code)
    print(response.text)

    assert response.status_code == 200

    response_json = response.json()

    # проверяем наличие ключей
    assert "profiles" in response_json
    assert "count" in response_json

    # profiles должен быть списком
    assert isinstance(response_json["profiles"], list)

    # count должен быть числом
    assert isinstance(response_json["count"], int)

    # список профилей не пустой
    assert len(response_json["profiles"]) > 0