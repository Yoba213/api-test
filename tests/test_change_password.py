import requests

from utils.api_helpers import (
    BASE_URL,
    LOGIN_URL,
    CHANGE_PASSWORD_URL,
)

def test_change_password(test_user):

    user_data, _ = test_user

    # логин пользователя
    login_response = requests.post(
        BASE_URL + LOGIN_URL,
        json={
            "username": user_data["username"],
            "password": user_data["password"]
        }
    )

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    headers = {
        "Authorization": f"Bearer {token}"
    }

    # новые данные пароля
    new_password = "NewPassword123"

    # запрос смены пароля
    response = requests.post(
        BASE_URL + CHANGE_PASSWORD_URL,
        headers=headers,
        json={
            "old_password": user_data["password"],
            "new_password": new_password
        }
    )

    print("CHANGE PASSWORD:")
    print(response.status_code)
    print(response.text)

    assert response.status_code == 200

    # проверяем логин с новым паролем
    new_login_response = requests.post(
        BASE_URL + LOGIN_URL,
        json={
            "username": user_data["username"],
            "password": new_password
        }
    )

    print("LOGIN WITH NEW PASSWORD:")
    print(new_login_response.status_code)
    print(new_login_response.text)

    assert new_login_response.status_code == 200