"""
Django settings for scrumboard project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=e-2fbsl6*70@lxij6h^uhivs$zk^@3k&tb*bp7ftks$8$2v^t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['localhost']

# Application definition

THIRD_PARTY_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tastypie',
)

PROJECT_APPS = (
    'scrumboard.board',
)

INSTALLED_APPS = THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'scrumboard.urls'

WSGI_APPLICATION = 'scrumboard.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'

LOG_PATH = os.path.join(os.path.dirname(BASE_DIR), 'django.log')
LOG_LEVEL = 'DEBUG'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s '
        },
        'request': {
            'format': '%(asctime)s %(levelname)s %(message)s. %(request_method)s: %(remote_addr)s%(path_info)s '
        }
    },
    'filters': {
        'request': {
            '()': 'django_requestlogging.logging_filters.RequestFilter',
        }
    },
    'handlers': {
        'logfile': {
            'level': LOG_LEVEL,
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_PATH,
            'formatter': 'simple',
            'maxBytes': 104857600,
            'backupCount': 100,
        },
        'requestfile': {
            'level': LOG_LEVEL,
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_PATH,
            'formatter': 'request',
            'filters': ['request'],
            'maxBytes': 104857600,
            'backupCount': 100,
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['logfile', 'mail_admins'],
            'level': LOG_LEVEL,
            'propagate': False
        },
        'items': {
            'handlers': ['requestfile', 'mail_admins'],
            'level': LOG_LEVEL,
            'propagate': False
        },
        '': {
            'handlers': ['logfile', 'mail_admins'],
            'level': LOG_LEVEL,
            'propagate': False
        }
    },
}
