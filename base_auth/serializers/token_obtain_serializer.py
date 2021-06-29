from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class AuthTokenObtainSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email

        return token
