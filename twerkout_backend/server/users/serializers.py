from rest_framework import serializers


class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField()
    age = serializers.IntegerField(required=False)
    weight = serializers.IntegerField(required=False)
    height = serializers.IntegerField(required=False)


class ProfileOutputSerializer(serializers.Serializer):
    username = serializers.CharField(source="user.username")
    age = serializers.IntegerField()
    weight = serializers.IntegerField()
    height = serializers.IntegerField()
