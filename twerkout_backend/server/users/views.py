from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from server.core.models import Profile
from server.core.services import register_user
from server.users.serializers import UserRegistrationSerializer, ProfileOutputSerializer


class UserRegistrationAPIView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def perform_action(self, username: str, password: str, **kwargs) -> None:
        register_user(username=username, password=password, **kwargs)

    def create(self, request: Request) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_action(**serializer.validated_data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProfileListAPIView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileOutputSerializer
    permission_classes = (AllowAny,)
