from pathlib import Path
from unittest.mock import DEFAULT
import os
import json
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-atqf!zyy+x-b(vwmb$db0*6e@-062+!d!cf6@%+$2hwh87#)0a"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "django.contrib.humanize",
    # 소셜 로그인 시 인증정보가 들어오는 사이트 관리
    "django.contrib.sites",
    # "community",
    "bulletin",
    "notice",
    "users",
    "music",
]

INSTALLED_APPS += [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.kakao',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.naver',
    ]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR,'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                # `allauth` needs this from django
                'django.template.context_processors.request',
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / 'static']

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# 로그인 성공 후 이동 URL 지정
# 장고의 로그인 기능을 이용하게 되면 로그인 성공 후 profile/ 로 이동하기 때문에
LOGIN_REDIRECT_URL = "/"
# 장고의 로그아웃 이후 원하는 곳으로 이동
LOGOUT_REDIRECT_URL = "/"

# 커스텀유저 모델 사용시
AUTH_USER_MODEL = "users.User"
# Custom User 모델 등록

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/" # http://127.0.0.1:8000/media/파일이름


# 네이버를 이메일 서버로 설정하기
DEFAULT_FROM_EMAIL = "lkj4086@naver.com"
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_HOST = "smtp.naver.com"
EMAIL_HOST_USER = "lkj4086"
EMAIL_HOST_PASSWORD = "djemals1324"
EMAIL_PORT = 465

# 구글 소셜 로그인을 위해서 google.json 읽어오기 

google = os.path.join(BASE_DIR,"google.json")
with open(google) as f:
    google = json.loads(f.read())

def get_social(setting, google = google):
    try:
        return google[setting]
    except KeyError:
        error_msg = 'set the {0} environment variable'.format(setting)
        raise ImproperlyConfigured(error_msg)

# 
SOCIALACCOUNT_PROVIDERS = {
    'google':{
        "APP":{
            'client_id' : get_social('client_id'),
            'secret' : get_social('client_secret'),
        },
        "SCOPE":{
            'profile',
            'email',
        },
        'AUTH_PARAMS':{
            'access_type':'offline',
        }
    }
}

SOCIALACCOUNT_LOGIN_ON_GET = True

SITE_ID = 2
# # 127.0.0.1 사이트 아이디
# SITE_ID = 2