from pathlib import Path
import os 
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(Path.joinpath(BASE_DIR, '.env'))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g4_@%m_65uy=flaq9m$apz2%ff_d(4b!)0t*(d$dcrylptwdw5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ALLOWED_HOSTS = ["localhost", "127.0.0.1", "213.199.58.201"]




INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = "/static/"

# Aquí Django va a copiar todos los estáticos cuando hagas collectstatic
STATIC_ROOT = BASE_DIR / "staticfiles"

# Opcional: carpeta global de estáticos (para desarrollo)
STATICFILES_DIRS = [
    BASE_DIR / "static",  # asegúrate que esta carpeta exista (aunque esté vacía)
]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"



CORS_ALLOW_ALL_ORIGINS = True # If this is used then `CORS_ALLOWED_ORIGINS` will not have any effect
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:20000",
    "http://127.0.0.1:20000",
    "http://213.199.58.201:20000",
    "https://barberia_grandfather.com",
]



CSRF_TRUSTED_ORIGINS = [
    "http://localhost:20000",
    "http://127.0.0.1:20000",
    "http://213.199.58.201:20000",
    "https://barberia_grandfather.com",
]

CORS_ALLOWED_ORIGIN_REGEXES = [
    "http://localhost:20000",
    "http://127.0.0.1:20000",
    "http://213.199.58.201:20000",
    "https://barberia_grandfather.com",
]






ROOT_URLCONF = 'sangarweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'sangarweb.wsgi.application'


import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "BarberDB",
        "USER": "postgres",
        "PASSWORD": "191011022",   # la que definiste en docker-compose
        "HOST": "213.199.58.201",
        "PORT": "5431",
    }
}


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


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Mexico_City'

USE_TZ = True



# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

