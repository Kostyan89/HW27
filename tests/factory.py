import factory
from ads.models import Ad, Category
from users.models import User


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    password = "123qwe"


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad
    id = factory.Sequence(lambda n: '%s' % n)
    name = "testtesttest"
    price = "1.00"
    address = "test"
    author = factory.SubFactory(UserFactory)
    description = "test"
    is_published = False
    category = None






