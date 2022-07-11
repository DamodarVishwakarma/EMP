from .base import *
import dj_database_url 


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


emp_dev  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(emp_dev)