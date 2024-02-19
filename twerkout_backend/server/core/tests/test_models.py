import pytest
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from server.core.models import UserManager, Profile

pytestmark = pytest.mark.django_db

User = get_user_model()


class TestUserManagerModel:
    username = "twerkin_skywalker"
    password = "nodadnobed123"

    def test_create_superuser(self):
        user_manager = UserManager()

        user = user_manager.create_superuser(username=self.username, password=self.password)

        assert user.username == self.username
        assert user.check_password(self.password) is True
        assert user.is_staff is True
        assert user.is_superuser is True


class TestUserModel:
    username = "twerkin_skywalker"
    password = "nodadnobed123"

    def test_token_is_present(self, user):
        expected_token = Token.objects.create(user=user)
        actual_token = user.auth_token

        assert actual_token == expected_token

    def test_token_is_absent(self, user):
        actual_token = getattr(user, "auth_token", None)

        assert actual_token is None
