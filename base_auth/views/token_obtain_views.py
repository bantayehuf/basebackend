from rest_framework_simplejwt.views import TokenObtainPairView
from base_auth.serializers.token_obtain_serializer import AuthTokenObtainSerializer

class AuthTokenObtainPairView(TokenObtainPairView):
    serializer_class = AuthTokenObtainSerializer