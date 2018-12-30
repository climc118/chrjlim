from .base import *

PRODUCTION = False
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'chrjlim',
        'USER': 'chrjlim',
        'PASSWORD': 'chrjlim',
        'HOST': '',
        'PORT': '',
    }
}

SECRET_KEY = 'ohwowthisissuchanunbreakablesecretkeysupersecretkeyobfuscationandallthat'
