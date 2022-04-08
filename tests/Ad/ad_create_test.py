from typing import List

import pytest
from faker import factory

from ads.models import Ad
from tests.factory import UserFactory


@pytest.mark.django_db
def test_ads_create(client, user, category, hr_token):
    response = client.post(
        "/ad/create/",
        {
            "is_published": False,
            "name": "testtesttest",
            "price": "1.00",
            "address": "test",
            "author": user.id,
            "category_id": category.id,
            "description": "test"

        },
        content_type="application/json",
        HTTP_AUTHORIZATION=f"Bearer {hr_token}")

    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "is_published": False,
        "name": "testtesttest",
        "price": "1.00",
        "description": "test",
        "address": "test",
        "image": None,
        "author": user.id,
        "category": category.id
    }

