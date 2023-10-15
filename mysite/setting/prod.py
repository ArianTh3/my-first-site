from mysite.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7aus290c6$3j3$lix=fdk=ifcjv0y%n5f8ihkbq3fju881+y(7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['theariankhademzadeh.ir', 'www.theariankhademzadeh.ir']

SITE_ID = 3

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'thearia1_Travel1',
        'USER': 'thearia1_arian',
        'PASSWORD': '09143533943Ar',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = BASE_DIR / 'static'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]


#CSRF_COOKIE_SECURE = True