from django.urls import path, include

from server.users import views

urlpatterns = [
    path("registration/", views.UserRegistrationAPIView.as_view()),
    path("", views.ProfileListAPIView.as_view()),
]
