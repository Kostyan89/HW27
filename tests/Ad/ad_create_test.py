import pytest

from users.models import User


@pytest.mark.django_db
def test_create_ad(client, hr_token):
    access_token, refresh_token = hr_token
    expected_response = {
        "id": 1,
        "name": "test",
        "price": 1,
        "is_published": "False",
        "author": user_id,
        "description": "test",
        "address": "test",
        "category": None,
        "image": None,
    }

    data = {
        "name": "test",
        "price": 1,
        "is_published": "False",
        "description": "test",
        "address": "test",
    }

    response = client.post(
        "/ad/create/",
        data,
        content_type="application/json",
        HTTP_AUTHORIZATION="Bearer " + access_token
    )

    assert response.status_code == 201
    assert response.data == expected_response


