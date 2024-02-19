import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

from server.core.models import Profile
from server.core.tests.factories import UserFactory

pytestmark = pytest.mark.django_db

User = get_user_model()


class TestUserRegistrationAPIView:
    ROUTE = "user-registration"
    username = "twerkin_skywalker"
    password = "nodadnobed123"
    age = 19
    weight = 72
    height = 173

    def test_register_user_with_mandatory_fields(self, api_client):
        response = api_client.post(
            reverse(self.ROUTE),
            data={
                "username": self.username,
                "password": self.password,
            }
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert Profile.objects.count() == 1
        profile = Profile.objects.first()
        assert getattr(profile.user, "auth_token", None) is not None
        assert profile.user.username == self.username
        assert profile.user.check_password(self.password) is True

    def test_register_user_with_all_fields(self, api_client):
        response = api_client.post(
            reverse(self.ROUTE),
            data={
                "username": self.username,
                "password": self.password,
                "age": self.age,
                "weight": self.weight,
                "height": self.height,
            }
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert Profile.objects.count() == 1
        profile = Profile.objects.first()
        assert profile.user.username == self.username
        assert profile.user.check_password(self.password) is True
        assert getattr(profile.user, "auth_token", None) is not None
        assert profile.age == self.age
        assert profile.weight == self.weight
        assert profile.height == self.height
