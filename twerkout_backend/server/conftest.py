import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from server.core.tests.factories import UserFactory

User = get_user_model()


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture
def user(db) -> User:
    return UserFactory()
