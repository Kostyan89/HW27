from rest_framework import serializers

from users.models import User, Location


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "role", "age", "locations"]


class UserRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    # locations = serializers.SlugRelatedField(
    #     required=False,
    #     many=True,
    #     read_only=True,
    #     slug_field='name'
    # )

    class Meta:
        model = User
        exclude = ['locations']

    # def is_valid(self, raise_exception=False):
    #     self._locations = self.initial_data.pop("locations")
    #     return super().is_valid(raise_exception=raise_exception)
    #
    # def create(self, validated_data):
    #     user = super().create(validated_data)
    #
    #     for location_name in self._locations:
    #         location, _ = Location.objects.get_or_create(name=location_name)
    #         user.location.add(location)
    #
    #     user.save()
    #     return user


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

