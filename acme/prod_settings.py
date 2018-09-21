import dj_database_url

from .settings import *

DEBUG = False
TEMPLATE_DEBUG = False

DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = [
    'acme-pro.herokuapp.com',
]

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
