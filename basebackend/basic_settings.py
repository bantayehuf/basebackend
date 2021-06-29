from os import path
from configparser import RawConfigParser
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

config = RawConfigParser()
config.read(path.join(BASE_DIR, 'conf.ini'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.get('secret', 'SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = config.get('debug', 'DEBUG')
DEBUG = True

ALLOWED_HOSTS = ('*',)

AUTH_USER_MODEL = 'base_auth.User'

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'base_auth',
    'rest_framework_simplejwt.token_blacklist',
)

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

DATABASES = {
    'default': {
        'ENGINE': config.get('db', 'ENGINE'),
        'NAME': config.get('db', 'NAME'),
        'USER': config.get('db', 'USER'),
        'PASSWORD': config.get('db', 'PASSWORD'),
        # Or an IP Address that your database is hosted on
        'HOST': config.get('db', 'HOST'),
        'PORT': config.get('db', 'PORT'),
        'OPTIONS': {
            'charset': config.get('db', 'CHAR_SET'),
            'use_unicode': True,
        },
    }
}

CORS_ALLOW_ALL_ORIGINS = True

'''CORS_URLS_REGEX = r'^/api/.*$'

CORS_ALLOWED_ORIGINS = [
    "https://example.com",
]
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]'''

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'SEARCH_PARAM':'q',
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(hours=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': True,

    'ALGORITHM': 'HS512',
    'SIGNING_KEY': config.get('secret', 'SIGNING_KEY'),
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'auth_type',

    'JTI_CLAIM': 'jti',
}
