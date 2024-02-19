from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_superuser(
        self,
        username: str,
        password: str,
    ):
        from server.core.services import create_user

        return create_user(
            username=username, password=password, is_staff=True, is_superuser=True
        )


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = "username"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True)
    weight = models.PositiveIntegerField(null=True)
    height = models.PositiveIntegerField(null=True)

    def __str__(self) -> tuple:
        return self.user.username, self.age
