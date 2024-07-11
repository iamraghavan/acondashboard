from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3x_tk9%b)wo6i&+_+msf-7%1&zzgp#ufptn7**k$@fc)4stm*@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['192.168.1.5', 'acondashboard.onrender.com', '127.0.0.1']

SESSION_COOKIE_AGE = 1209600  # 2 weeks
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webdashboard',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'webdashboard.middleware.JWTAuthMiddleware',
]

ROOT_URLCONF = 'acondashboard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'acondashboard.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

BASE_DIR = Path(__file__).resolve().parent.parent

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'u427691722_jbl',           # Replace with your database name
        'USER': 'u427691722_adminjbl',      # Replace with your database username
        'PASSWORD': 'p!T4X5#9RjE2',         # Replace with your database password
        'HOST': '195.179.239.102',          # Replace with your database host
        'PORT': '3306',                     # Replace with your database port if different
    }
}

# Firebase configuration
FIREBASE_CONFIG = {
    'apiKey': 'AIzaSyCgoz33SSJnA1Qu2Ah3FOYJbe6-48wkwzo',
    'authDomain': 'andavarcon.firebaseapp.com',
    'databaseURL': 'https://andavarcon-default-rtdb.asia-southeast1.firebasedatabase.app',
    'projectId': 'andavarcon',
    'storageBucket': 'andavarcon.appspot.com',
    'messagingSenderId': '345505940170',
    'appId': '1:345505940170:web:5f4d99483f4b0ff9ca2a33',
    'measurementId': 'G-S11Y6KNMT4'
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'webdashboard/static'),
    os.path.join(BASE_DIR, 'acondashboard/static'),

]

# Use default storage to skip missing files errors
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'static/js/serviceworker.js')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Path to your Firebase admin SDK JSON file
FIREBASE_ADMIN_SDK_PATH = os.path.join(BASE_DIR, 'static', 'andavarcon-firebase-adminsdk.json')


# Use default storage to skip missing files errors
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'




