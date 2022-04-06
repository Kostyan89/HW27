import factory
from ads.models import Ad
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    password = "123qwe"


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = "test"
    price = 1
    address = "test"
    author = factory.SubFactory(UserFactory)
    description = "test"
    is_published = "False"
