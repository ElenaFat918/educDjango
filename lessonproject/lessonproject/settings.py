"""
Django settings for lessonproject project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ps8o=cbjgu$*fdmrs!9r5fea&j@b5!zu1!n#5lh^@ilh!#+^ou'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    '192.168.1.102',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lessonapp',
    'myapp2',
    'myapp3',
    'myapp4',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lessonproject.urls'

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

WSGI_APPLICATION = 'lessonproject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

"""
● version: версия формата конфигурации логирования. 
    В настоящее время используется версия 1. 
● disable_existing_loggers: если значение равно True, то все существующие логгеры будут отключены.
    Если значение равно False, то существующие логгеры будут продолжать работать.
● handlers: определяет, какие обработчики будут использоваться для записи логов. 
    Обработчики могут быть консольными или файловыми. 
● loggers: определяет, какие логгеры будут использоваться для записи логов. 
    Логгеры могут быть определены для фреймворка Django или для конкретного приложения.  
    Для каждого обработчика и логгера можно указать следующие параметры: 
● class: класс, который будет использоваться для записи логов. 
    В нашем примере мы используем классы StreamHandler и FileHandler для записи логов в консоль
    и файл соответственно. 
● filename: путь к файлу, в который будут записываться логи. 
    В нашем примере мы записываем логи в файл /path/to/django.log.   
    Внимание! Каталог path/ и вложенный в него каталог to/ необходимо создать самостоятельно.
    Либо исправьте значение на django.log, чтобы создать файл логов в корневой директории проекта.  
● level: минимальный уровень логирования, который будет записываться. 
    В нашем примере мы указали уровень INFO для логгера django и уровень DEBUG для логгера lessonapp. 
● propagate: если значение равно True, то сообщения будут передаваться родительским логгерам. 
    Если значение равно False, сообщения не будут передаваться родительским логгерам.
"""
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {'format': '{levelname} {asctime} {module} {process} {thread} {message}',
                    'style': '{',
                    },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',  # добавлен параметр formatter
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': './log/django.log',
            'formatter': 'verbose',  # добавлен параметр formatter
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
        'lessonapp': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
