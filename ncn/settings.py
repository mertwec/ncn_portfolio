"""
Django settings for ncn project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

import django.middleware.cache
from dotenv import load_dotenv
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = BASE_DIR / 'ncn'

# load var_environment
load_dotenv(os.path.join(BASE_DIR, ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    'django-insecure-w5hk*a-dqqz$_id*l1pax7t#7z(sryzaj(30k5$rfp7=1o+fte'
) 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', '1').lower() in ['true', 't', '1']


ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(' ')

ADMIN_USER = {
    "login": os.getenv('ADMIN_LOGIN'),
    "password": os.getenv('ADMIN_PASSWORD')
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'notes.apps.NotesConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',       # connect whitenoise for static
    # 'django.middleware.http.ConditionalGetMiddleware',  # for client cache
    'django.middleware.cache.UpdateCacheMiddleware',    # for server cache
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',   # for server cache
]

ROOT_URLCONF = 'ncn.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'notes.midlewares.categories_sites',
                'notes.midlewares.quotes_random'
            ],
        },
    },
]

WSGI_APPLICATION = 'ncn.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.parse(os.getenv("DATABASE_URL"),conn_max_age=600)
    # {
    #     "ENGINE": "django.db.backends.postgresql",
    #     "NAME": "ncn_portfolio_db",
    #     'USER': os.getenv("USER_POSTGRES", 'postgres'),
    #     'PASSWORD': os.getenv("PASSWORD_POSTGRES"),
    #     'HOST': 'localhost',
    #     'PORT': '',
    # }
    
    # 'sqlite': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': PROJECT_DIR / 'database/crib_db.sqlite3',
    # }
}

DATABASES_QUOTER = os.path.join(PROJECT_DIR, "database", "quotes.json")

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGIN_URL = "/user/login/"
LOGIN_REDIRECT_URL = "/"

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STORAGES = {
    # for django >= 4.2
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' # for django < 4.2
 
# any files for static files
STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, "static_conect"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "static_conect", "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "static_conect", "media")

DUMP_FILE = "sites.json"
DUMP_DB_PATH = os.path.join(BASE_DIR, "static_conect", "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CACHES = {
    'default': {
        'BACKEND': "django.core.cache.backends.filebased.FileBasedCache",
        'LOCATION': BASE_DIR / 'cache_file',
        'TIMEOUT': 300,
    }
}
