from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'emp_dev',
        'USER': 'postgres',
        'PASSWORD': 'postgresql',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}