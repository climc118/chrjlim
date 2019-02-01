from .base import *

PRODUCTION = True
DEBUG = False
ALLOWED_HOSTS = ['chrjlim.cepxmm978p.us-east-2.elasticbeanstalk.com']

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
