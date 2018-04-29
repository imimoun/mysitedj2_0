# coding: utf-8
"""Settings for Travis."""

# List: use split for getting a list
ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "patient_engine_test",
        'USER': "postgres",
        'PASSWORD': "",
        'HOST': "localhost",
        'PORT': "5432",
    }
}
