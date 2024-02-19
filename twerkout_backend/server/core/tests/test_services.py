import pytest
from django.contrib.auth import get_user_model

from server.core.services import create_user, register_user

pytestmark = pytest.mark.django_db

User = get_user_model()


class TestCreateUserService:
    username = "twerkin_skywalker"
    password = "nodadnobed123"

    def test_create_user_success(self):
        user = create_user(username=self.username, password=self.password)

        assert User.objects.filter(id=user.id).first() == user


class TestRegisterUserService:
    username = "twerkin_skywalker"
    password = "nodadnobed123"
    age = 19
    weight = 72
    height = 173

    def test_create_user_success(self):
        profile = register_user(username=self.username, password=self.password, age=self.age, weight=self.weight, height=self.height)

        assert profile.user.username == self.username
        assert profile.user.check_password(self.password) is True
        assert profile.age == self.age
        assert profile.weight == self.weight
        assert profile.height == self.height
        assert getattr(profile.user, "auth_token", None) is not None
