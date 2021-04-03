"""
Django settings for daily_salary project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import datetime

ENV = os.environ.get('CORE_ENV')
CORE_SENDGRID_API_KEY = os.environ.get('CORE_SENDGRID_API_KEY')
CORE_KALEYRA_API_KEY = os.environ.get('CORE_KALEYRA_API_KEY')
CORE_QUESS_PARTNER_KEY = os.environ.get("CORE_QUESS_PARTNER_KEY", 'aute6ca9x9kwAgkXHj8PnuYnb8g7N7YD')
CORE_FCM_SERVER_KEY = os.environ.get('CORE_FCM_SERVER_KEY')
CORE_X_KARZA_KEY = os.environ.get('CORE_X_KARZA_KEY', 'D3q9DgU7XkLni3fx')

#Quess Attendance API Authorization Token
CORE_QUESS_AUTH_TOKEN = os.environ.get('CORE_QUESS_AUTH_TOKEN', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3ZWRnZXJldGFpbC5jb21cL2FwaVwvdjFcL2xvZ2luIiwiaWF0IjoxNjE1OTYzNTQwLCJleHAiOjE2MTU5OTk1NDAsIm5iZiI6MTYxNTk2MzU0MCwianRpIjoiN3kyMzhWS1l6N2dURzBRUSIsInN1YiI6MSwicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.dKA8n9hctN7oT5EGlSd6YGSNASaRYWZgF_7304trdaY')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('CORE_SECRET_KEY', 'aa3cbv24tn$4tvmn-b4d161vk(6q$3!m5r=^%t##dpff&_#$fk')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('CORE_DEBUG', True)

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'workers.apps.WorkersConfig',
    'pages.apps.PagesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jquery',
    'bootstrap4',
    'authentication.apps.AuthenticationConfig',
    'tags.apps.TagsConfig',
    'django_rq',
    'rest_framework',
    'core',
    'corsheaders',
    'django_extensions',
    'drf_yasg2',
    'dynamic_validator',
    'django_cleanup',
    'fcm_django',
    'django_crontab',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'daily_salary.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'daily_salary.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if ENV == "production":
    BASE_URL = 'dailysalary.in'
    PG_BASE_URL = "https://pg.dailysalary.in"
    KYC_BASE_URL = "https://kyc.dailysalary.in"
else:
    BASE_URL = 'staging.dailysalary.in'
    PG_BASE_URL = "https://staging-pg.dailysalary.in"
    KYC_BASE_URL = "https://staging-kyc.dailysalary.in"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('CORE_DB_NAME','instasalary'),
        'USER': os.environ.get('CORE_DB_USER', 'instasalary'),
        'PASSWORD': os.environ.get('CORE_DB_PASS', 'insta@123'),
        'HOST': os.environ.get('CORE_DB_HOST','localhost'),
        'PORT': os.environ.get('CORE_DB_PORT','5432'),
    }
}

CRONJOBS = [
    # ('0 9 * * *', 'background_jobs.send_auto_credited_email_everyday'),
    # ('0 10 * * 1', 'background_jobs.send_viral_loop_email'),
    # ('59 23 * * *', 'background_jobs.create_subscription_statement_at_last_day_of_month'),
    ('30 10 26-31 * *', 'background_jobs.month_end_notification'),
    ('1 0 1 * *', 'background_jobs.reset_employee_at_every_first_day_of_month'),
    # ('0 9 * * *', 'background_jobs.collect_repayment'),
    # ('0 7 * * *', 'background_jobs.fetch_quess_attendance_daily'),
]

FCM_DJANGO_SETTINGS = {
        "FCM_SERVER_KEY": CORE_FCM_SERVER_KEY
     }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

LOGIN_REDIRECT_URL = 'workers:index'
LOGOUT_REDIRECT_URL = 'home'

AUTH_USER_MODEL = 'authentication.User'

RQ_QUEUES = {
    'default': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
        'PASSWORD': '',
        'DEFAULT_TIMEOUT': 360,
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',)
}
SWAGGER_SETTINGS = {
    'DEFAULT_FIELD_INSPECTORS': [
        'drf_yasg2.inspectors.InlineSerializerInspector',
    ],
    'DEFAULT_MODEL_RENDERING': [
        'example',
    ],
    'SUPPORTED_SUBMIT_METHODS': [
        'get',
        'put',
        'post',
        'patch',
    ],
    'SECURITY_DEFINITIONS': {
      'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
      }
    }
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=7),
}

# CORS ALLOWED
CORS_ORIGIN_ALLOW_ALL=True
# SSL CONFIG
if ENV == 'Production':
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    #SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True


MEDIA_ROOT = os.path.join(BASE_DIR, 'images')
MEDIA_URL = '/images/'
