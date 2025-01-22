"""
Django settings for backend project.
"""

import os
from pathlib import Path
from pymongo import MongoClient

# Environment detection
ENV = os.environ.get('DJANGO_ENV', 'development')

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent  # Adjust this if needed

# Security
SECRET_KEY = os.environ.get('SECRET_KEY')  # Remove default value in production!
DEBUG = ENV == 'development'
ALLOWED_HOSTS = ['*'] if DEBUG else [
    'nifty50-backend.onrender.com',  # Your Render.com hostname
    'your-production-domain.com'
]

# ================== Application Definition ==================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party
    'rest_framework',
    'corsheaders',
    'django_filters',
    
    # Local apps
    'apps.users',
    'apps.alerts',
    'apps.analysis',
    'apps.nifty_data',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

# ================== Database Configuration ==================
# PostgreSQL for Django internals (production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    }
}

# MongoDB for application data
MONGO_URI = os.environ.get('MONGO_URI')
MONGO_DB_NAME = os.environ.get('MONGO_DB_NAME', 'nifty50')
mongo_client = MongoClient(MONGO_URI)
mongo_db = mongo_client[MONGO_DB_NAME]

# ================== Authentication & Users ==================
AUTH_USER_MODEL = 'users.CustomUser'

# ================== REST Framework ==================
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

# ================== Security Headers ==================
if not DEBUG:
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# ================== CORS ==================
CORS_ALLOW_ALL_ORIGINS = False  # Always false in production
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://your-frontend-domain.com"
]

# ================== Environment Variables ==================
# Add these to Render.com environment variables
# POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST
# MONGO_URI, MONGO_DB_NAME
# SECRET_KEY, CELERY_BROKER_URL, NEWS_API_KEY, etc.