from .base import *

PRODUCTION = True
DEBUG = False
ALLOWED_HOSTS = ['chrjlim.vtv7ryjz3f.us-east-1.elasticbeanstalk.com']

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

SECRET_KEY = 'ajd232pmxmkadf9ebwosqkxqpklancbvwoiefnij42nkn6kkjca'
