import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '+k*kdcv4ut*bd99nb(ox$%j_9(1#8@_)!aa4oy2%iwsg&!tt15'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['localhost',
                 '127.0.0.1']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dziekanat.urls'

WSGI_APPLICATION = 'dziekanat.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ntr',
        'USER': 'postgres',
        'PASSWORD': 'qwerty1asd',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}

LANGUAGE_CODE = 'pl-pl'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
