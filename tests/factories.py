# pylint: disable=too-few-public-methods
"""
Test Factory to make fake objects for testing
"""
import factory
from factory.fuzzy import FuzzyChoice, FuzzyDecimal
from service.models import Product, Category


class ProductFactory(factory.Factory):
    """Creates fake products for testing"""

    class Meta:
        """Maps factory to data model"""
        model = Product

    id = factory.Sequence(lambda n: n)
    name = factory.Faker("first_name")
    description = factory.Faker("sentence")
    price = FuzzyDecimal(0.5, 2000.00, 2)
    available = FuzzyChoice(choices=[True, False])
    category = FuzzyChoice(choices=list(Category))
