from .base import *

DEBUG = False
ALLOWED_HOSTS = ["*"]
CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
    "https://univway.com"
]

MIDDLEWARE += [
    "whitenoise.middleware.WhiteNoiseMiddleware"
]
INSTALLED_APPS += [
    "whitenoise.runserver_nostatic"
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
