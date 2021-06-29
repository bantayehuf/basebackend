from rest_framework import filters as rest_filters
from rest_framework import generics, serializers
from base_auth.lib.response import ResponseMessage


def filter_multiple_lookups(lookup_fields=None, request_fields=None):
    if lookup_fields is None:
        raise serializers.ValidationError(
            {'error': ['Lookups filed is not given.']})
    elif request_fields is None:
        raise serializers.ValidationError(
            {'error': ['Request field is not given.']})

    filter = {}
    field_not_defined = {}
    for field in lookup_fields:
        # Ignore empty fields.
        if request_fields.get(field) != None and str(request_fields.get(field)).strip() != '':
            filter[field] = request_fields[field]
        else:
            field_not_defined[field] = ['This field is required.']

    if len(field_not_defined) > 0:
        raise serializers.ValidationError(field_not_defined)

    return filter


def check_forbidden_fields(allowed_fields=None, request_fields=None):
    if allowed_fields is None:
        raise serializers.ValidationError(
            {'error': ['Allowed fields is not listed.']})

    forbidden_fields = {}
    try:
        for field in request_fields:
            if not field in allowed_fields:
                forbidden_fields[field] = ['Field Not Allowed.']
    except:
        raise serializers.ValidationError({'error': ['Forbidden.']})

    if len(forbidden_fields) > 0:
        raise serializers.ValidationError(forbidden_fields)

    return True


class CreateObject(generics.GenericAPIView):

    allowed_fields = None

    def create_object(self, request, *args, **kwargs):

        check_forbidden_fields(
            allowed_fields=self.allowed_fields,
            request_fields=request.data
        )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return [201]


class UpdateObject(generics.GenericAPIView):
    object_model = None
    allowed_fields = None

    def update_object(self, request, *args, **kwargs):

        if request.query_params.get('id') == None or str(request.query_params.get('id')).strip() == '':
            raise serializers.ValidationError(
                {'id': ['This field is required on query parameter.']}
            )

        if len(request.data) < 1:
            raise serializers.ValidationError(
                {'error': ['Bad request.']}
            )

        check_forbidden_fields(
            allowed_fields=self.allowed_fields,
            request_fields=request.data
        )

        try:

            id = int(request.query_params['id'])
            student = self.object_model.objects.get(id=id)
        except ValueError:
            raise serializers.ValidationError(
                {'id': ['Enter a valid id.']}
            )
        except self.object_model.DoesNotExist:
            return [404]
        except KeyError:
            return [403]
        except Exception:
            return [500]

        serializer = self.get_serializer(
            student, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return [200]

    def put(self, request, *args, **kwargs):
        return ResponseMessage(status_code=405)


class DeleteObject(generics.GenericAPIView):
    object_model = None
    allowed_fields = None

    def delete_object(self, request, *args, **kwargs):
        if request.query_params.get('id') == None or str(request.query_params.get('id')).strip() == '':
            raise serializers.ValidationError(
                {'id': ['This field is required on query parameter.']}
            )

        check_forbidden_fields(
            allowed_fields=self.allowed_fields,
            request_fields=request.query_params
        )

        try:
            id = int(request.query_params['id'])
            student = self.object_model.objects.get(id=id)
            student.delete()
        except ValueError:
            raise serializers.ValidationError(
                {'id': ['Enter a valid id.']}
            )
        except self.object_model.DoesNotExist:
            return [404]
        except KeyError:
            return [403]
        except Exception:
            return [500]

        return [200]


class GetAllObjects(generics.GenericAPIView):

    def object_list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        response_data = serializer.data

        if len(response_data) == 0:
            return [404]

        return [200, response_data]


class GetSearchedObject(generics.GenericAPIView):

    filter_backends = [rest_filters.SearchFilter]

    def search_object(self, request, *args, **kwargs):

        search = request.query_params.get('q')
        if search is None or str(search).strip() == '':
            return [400]

        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return [404]

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        response_data = serializer.data

        return [200, response_data]
