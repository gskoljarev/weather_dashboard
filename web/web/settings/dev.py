from base import *

DEBUG = True


# Database

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES = {'default': dj_database_url.config()}
DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'


# Applications

INSTALLED_APPS += [
    'django_extensions',
]