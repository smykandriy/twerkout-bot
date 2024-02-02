from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from server.core.models import Profile

User = get_user_model()


def create_user(username: str, password: str, **kwargs) -> User:
    user = User.objects.create(username=username, **kwargs)
    user.set_password(password)
    user.save()
    Token.objects.create(user=user)
    return user


def register_user(username: str, password: str, **kwargs) -> Profile:
    user = create_user(username=username, password=password)
    profile = Profile.objects.create(user=user, **kwargs)
    return profile
