from pytest_factoryboy import register

from tests.factory import AdFactory, UserFactory

pytest_plugins = "tests.fixtures"


register(AdFactory)
register(UserFactory)
