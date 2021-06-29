from rest_framework import serializers
from base_auth.models import User
from base_auth.lib.serializers import(
    CreateSerializer,
    UpdateSerializer,
    FetchSerializer
)


class CreateUserSerializer(CreateSerializer):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'middle_name',
            'email',
            'password',
        )
        extra_kwargs = {
            'password': {'write_only': False},
        }

    def create(self, validated_data):
        user = User(
            first_name=validated_data.get('first_name'),
            middle_name=validated_data.get('middle_name'),
            last_name=validated_data.get('last_name'),
            email=validated_data.get('email'),
        )

        user.set_password(validated_data.get('password'))
        user.save()

        return user


class UpdateUserSerializer(UpdateSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'middle_name',
            'email',
            'password',
            'is_active',
        )
        extra_kwargs = {
            'password': {'write_only': False},
        }

    def update(self, instance, validated_data):

        instance.first_name = validated_data.get(
            'first_name', instance.first_name
        )
        instance.middle_name = validated_data.get(
            'middle_name', instance.middle_name
        )
        instance.last_name = validated_data.get(
            'last_name', instance.last_name
        )
        instance.email = validated_data.get(
            'email', instance.email
        )
        instance.is_active = validated_data.get(
            'is_active', instance.is_active
        )

        if validated_data.get('password') != None and validated_data.get('password').strip() != '':
            instance.set_password(validated_data.get('password'))

        instance.save()

        return instance


class FetchUserSerializer(FetchSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'full_name',
            'email',
            'is_active',
            'date_joined',
        )#'last_login',
