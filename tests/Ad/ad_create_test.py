from typing import List

import pytest
from faker import factory

from ads.models import Ad
from tests.factory import UserFactory


@pytest.mark.django_db
def test_ads_create(client, user, category):
    assert not Ad.objects.all()
    response = client.post(
        "/ad/create/",
        {
            "is_published": False,
            "name": "testtesttest",
            "price": "1.00",
            "address": "test",
            "author": user.id,
            "category_id": category.id,
            "description": None

        },
        content_type="application/json",
    )
    ads: List[Ad] = Ad.objects.all()
    assert len(ads) == 1

    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "is_published": False,
        "name": "testtesttest",
        "price": "1.00",
        "description": None,
        "address": "test",
        "image": None,
        "author": user.id,
        "category": 1
    }

