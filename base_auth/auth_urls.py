from django.urls import path
from django.urls.conf import include
from base_auth.views import user_views
from rest_framework_simplejwt.views import TokenRefreshView
from base_auth.views.token_obtain_views import AuthTokenObtainPairView

user_management_urls = ([
    path('create', user_views.CreateUser.as_view(), name='create_user'),
    path('update', user_views.UpdateUser.as_view(), name='update_user'),
    path('delete', user_views.DeleteUser.as_view(), name='delete_user'),
    path('list', user_views.ViewAllUsers.as_view(), name='list_users'),
    path('search', user_views.ViewSearchedUser.as_view(), name='search_users'),
], 'user')

app_name = 'base_auth'
urlpatterns = [
    path('login', AuthTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token-refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', include(user_management_urls))
]
