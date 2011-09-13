import logging
import os
import os.path
import socket
import json
import unicodedata

HOST = socket.gethostname()
MAINDIR = os.path.dirname(os.path.abspath( __file__ ))
LOGIN_URL = "/login/"
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'


if HOST == 'web187.webfaction.com':
    filename = os.path.join(MAINDIR, "serverconf.json")
    with open(filename) as conf_file:
        serverconf = json.load(conf_file)

    PRODUCTION = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'visimus',
            'USER': 'visimus',
            'PASSWORD': serverconf['db-password'],
            'HOST': '127.0.0.1',
            'PORT': '5432',
            }
        }

    SEND_BROKEN_LINK_EMAILS = False
    EMAIL_HOST = 'smtp.webfaction.com'
    EMAIL_HOST_USER = 'kroger'
    password = serverconf['email-password']
    EMAIL_HOST_PASSWORD = unicodedata.normalize('NFKD', password).encode('ascii','ignore')
    DEFAULT_FROM_EMAIL = 'kroger@pedrokroger.net'
    SERVER_EMAIL = DEFAULT_FROM_EMAIL

    LOGFILE = os.path.join(MAINDIR, 'log', 'visimus.log')
    STATIC_ROOT = '/home/kroger/webapps/visimus_static/'
    MEDIA_ROOT = ''

else:
    PRODUCTION = False
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(MAINDIR, 'data.db'),
            }
        }

    LOGFILE = os.path.join(MAINDIR, 'log', 'visimus.log')
    STATIC_ROOT = os.path.join(MAINDIR, "testapp/static/")


if PRODUCTION:
    DEBUG = False
    TEMPLATE_DEBUG = DEBUG
    LOG_LEVEL = logging.DEBUG
else:
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG
    LOG_LEVEL = logging.DEBUG


ADMINS = (
    ('Pedro Kroger', 'kroger@pedrokroger.net'),
)

MANAGERS = ADMINS

TIME_ZONE = 'America/Bahia'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

SECRET_KEY = '2#t0gkj0w_1nn&jq!(a68q*50d#t41!btf6s44#+v7$czw-187'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'visimus.urls'

TEMPLATE_DIRS = (
    os.path.join(MAINDIR, 'visimus', 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.static',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.staticfiles',
    'visimus.matrix',
    'south',
    'django_nose',
    )


TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--color',
    '--with-coverage',
    '--cover-package=testapp',
    '--cover-html',
    '--nologcapture',
]

AUTH_PROFILE_MODULE = "testapp.UserProfile"

logging.basicConfig(filename=LOGFILE,level=LOG_LEVEL,
                    format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)
