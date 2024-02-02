from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class UserBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        user_model = get_user_model()

        if not username:
            username = kwargs.get("username")

        if not (user := user_model.objects.filter(username=username).first()):
            return None

        if user.check_password(password):
            return user

    def get_user(self, user_id):
        user_model = get_user_model()
        return user_model.objects.filter(pk=user_id).first()
