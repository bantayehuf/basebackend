from rest_framework import serializers


class CreateSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):

        raise serializers.ValidationError(
            {'error': ['Create object serializer could not be used to update']}
        )


class UpdateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        raise serializers.ValidationError(
            {'error': ['Fetch object serializer could not be used to create']}
        )


class FetchSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        raise serializers.ValidationError(
            {'error': ['Fetch object serializer could not be used to create']}
        )

    def update(self, instance, validated_data):
        raise serializers.ValidationError(
            {'error': ['Fetch object serializer could not be used to update']}
        )
