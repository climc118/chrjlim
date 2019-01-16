from .base import *

PRODUCTION = True
DEBUG = False
ALLOWED_HOSTS = ['chrjlim.f7zedgcfji.us-west-2.elasticbeanstalk.com']

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
