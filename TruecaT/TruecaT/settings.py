# encoding:utf-8

"""
Django settings for TruecaT project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
RUTA_PROYECTO = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k6g=78clwnhcg)q!v!k%6n$+3z(q^1i7ifhi%qjyvczxdg2wv%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

ADMINS = (
('David Sanchez','i22safed@uco.es'),
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'principal',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.sqlite3', # Add ‘postgresql_psycopg2’,
    'NAME': os.path.join(RUTA_PROYECTO, 'db.sqlite3'), # Or path to database file if using sqlite3.
    'USER': '', # Not used with sqlite3.
    'PASSWORD': '', # Not used with sqlite3.
    'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
    'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

ROOT_URLCONF = 'TruecaT.urls'

WSGI_APPLICATION = 'TruecaT.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = (
    os.path.join(RUTA_PROYECTO,'TruecaT/templates'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


SITE_ID = 1


STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(RUTA_PROYECTO,"static"),
    )
