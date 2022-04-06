import pytest

from ads.serializers import AdListSerializer
from tests.factory import AdFactory


@pytest.mark.django_db
def test_ad_list(client):
    ads_list = AdFactory.create_batch(10)
    ads = []
    for ad in ads_list:
        ads.append({
            "id": ad.id,
            "author": None,
            "author_id": ad.author_id,
            "name": ad.name,
            "price": '1.00',
            "description": "test",
            "category_id": None,
            "is_published": False,
            "image": None
        })

    expected_response = {
        "items": ads,
        "num_pages": 1,
        "total": 10,
    }
    response = client.get("/ad/")

    assert response.status_code == 200
    assert response.json() == expected_response
