from rest_framework.response import Response
from rest_framework import serializers

from base_auth.lib.response import ResponseMessage
from base_auth.lib.generics import (
    CreateObject,
    UpdateObject,
    DeleteObject,
    GetAllObjects,
    GetSearchedObject,
)

from base_auth.models.user_models import User
from base_auth.serializers.user_serializer import(
    CreateUserSerializer,
    UpdateUserSerializer,
    FetchUserSerializer,
)


class CreateUser(CreateObject):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

    allowed_fields = (
        'first_name',
        'middle_name',
        'last_name',
        'email',
        'password',
    )

    def post(self, request, *args, **kwargs):
        response_data = self.create_object(request, *args, **kwargs)

        if response_data[0] != 201:
            return ResponseMessage(status_code=406)

        return ResponseMessage(status_code=201)


class UpdateUser(UpdateObject):

    object_model = User
    serializer_class = UpdateUserSerializer
    allowed_fields = (
        'first_name',
        'middle_name',
        'last_name',
        'email',
        'password',
        'is_active',
    )

    def patch(self, request, *args, **kwargs):

        if 'is_active' in request.data and str(request.data.get('is_active')).strip() == '':
            raise serializers.ValidationError(
                {'is_active': ['This field may not be blank.']}
            )

        response_data = self.update_object(request, *args, **kwargs)
        return ResponseMessage(status_code=response_data[0])


class DeleteUser(DeleteObject):
    object_model = User
    allowed_fields = ('id',)

    def delete(self, request, *args, **kwargs):
        response_data = self.delete_object(request, *args, **kwargs)
        return ResponseMessage(status_code=response_data[0])


class ViewAllUsers(GetAllObjects):

    queryset = User.objects.all()

    serializer_class = FetchUserSerializer

    def get(self, request, *args, **kwargs):

        response_data = self.object_list(request, *args, **kwargs)

        if response_data[0] != 200:
            return ResponseMessage(status_code=response_data[0])

        return Response(response_data[1])


class ViewSearchedUser(GetSearchedObject):
    queryset = User.objects.all()
    serializer_class = FetchUserSerializer

    search_fields = ('email', 'first_name', 'middle_name', 'last_name',)

    def get(self, request, *args, **kwargs):

        response_data = self.search_object(request, *args, **kwargs)
        if response_data[0] != 200:
            return ResponseMessage(status_code=response_data[0])

        return Response(response_data[1])
