from utils.api_helpers import login


def test_login_api(test_user):

    user_data, _ = test_user

    response = login(
        user_data["username"],
        user_data["password"]
    )

    print("TEST LOGIN:")
    print(response.status_code)
    print(response.text)

    assert response.status_code == 200

    response_json = response.json()

    assert "access_token" in response_json
    assert response_json["access_token"] is not None