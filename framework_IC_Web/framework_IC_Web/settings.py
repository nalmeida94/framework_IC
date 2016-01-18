"""
Django settings for framework_IC_Web project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dpjo2svbo+do9xjdm8d%pvptb3tobnvoe)g0p+lqo*$i)to6&_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Datasource',
    'Node',
    'Radio',
    'Snapshot',
    'Tag',
    'Values',

    'gcharts',
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

ROOT_URLCONF = 'framework_IC_Web.urls'

WSGI_APPLICATION = 'framework_IC_Web.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,"framework_IC_Web", "static", "templates"),
)

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

## NO WINDOWS
DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.mysql',
        #'ENGINE': 'mysql.connector.django',        
        'NAME': 'bdic',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
          'autocommit': True,
        },
    }
}
## NO SUSE
'''
DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME': 'bdic',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',        
    }
}
'''

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR,"framework_IC_Web", "static", "media")

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR,"framework_IC_Web", "static", "static-only")

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,"framework_IC_Web", "static", "static"),
    )
