import factory

from api.models import Client


@factory.Faker.override_default_locale('fr_FR')
class ClientFactory(factory.django.DjangoModelFactory):
    """
        Class for creating a fake instance of the Invoice model.
        You'll need to provide an existing data source instance.
    """
    class Meta:
        model = Client

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    city = factory.Faker('city')
    postal_code = factory.Faker('postcode')
    gender = factory.Faker('boolean')
