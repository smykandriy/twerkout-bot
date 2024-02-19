from django.contrib.auth import get_user_model
from factory import Sequence, SubFactory
from factory.django import DjangoModelFactory
from faker import Faker

from server.core.models import Profile

faker = Faker()

User = get_user_model()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = Sequence(lambda x: faker.user_name())
    password = "daddyinbeddy"


class ProfileFactory(DjangoModelFactory):
    class Meta:
        model = Profile

    user = SubFactory(UserFactory)
