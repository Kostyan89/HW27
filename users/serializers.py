from rest_framework import serializers

from users.models import User, Location


class CheckRamblerEmail:
    def __call__(self, value):
        if not value.endswith("rambler.ru"):
            raise serializers.ValidationError("Rambler user can't register")


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "age", "locations"]


class UserRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[CheckRamblerEmail])

    class Meta:
        model = User
        exclude = ['locations']

    def save(self):
        user = super().save()
        user.set_password(user.password)
        user.save()
        return user


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

