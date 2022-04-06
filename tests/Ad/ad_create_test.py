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
            "price": None,
            "address": None,
            "author": user.id,
            "category_id": None,
            "description": None

        },
        content_type="application/json",
    )
    ads: List[Ad] = Ad.objects.all()
    assert len(ads) == 1

    assert response.status_code == 201
    assert response.json() == {
        "id": ads[0].pk,
        "is_published": False,
        "name": "testtesttest",
        "price": None,
        "description": None,
        "address": None,
        "image": None,
        "author": user.id,
        "category_id": None
    }

