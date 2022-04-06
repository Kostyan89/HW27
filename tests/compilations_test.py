from typing import List

import pytest

from ads.models import Compilation


@pytest.mark.django_db
def test_compilation_create(client, hr_token, user, ad):
    response = client.post(
        "/comp/create/",
        {
            "name": "test compilation",
            "owner": user.id,
            "items": [ad.id]
        },
        content_type="application/json",
        HTTP_AUTHORIZATION=f"Bearer {hr_token}")
    compilation: List[Compilation] = Compilation.objects.all()
    assert len(compilation) == 1

    assert response.status_code == 201
    assert response.json() == {"id": compilation[0].pk, "name": "test compilation", "owner": user.id, "items": [ad.id]}
