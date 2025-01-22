import os
from pymongo import MongoClient

# Django dummy database (required)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy',
    }
}

# PyMongo setup for MongoDB
mongo_client = MongoClient(os.getenv('MONGO_URI', 'mongodb+srv://lakshvarma6:your_password@nifty-mongo.5ztn7.mongodb.net/?retryWrites=true&w=majority&appName=nifty-mongo'))
mongo_db = mongo_client[os.getenv('MONGO_DB_NAME', 'nifty50')]

# Remove auth/admin/sessions if unused
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'rest_framework',          # If you use Django REST Framework
    'corsheaders',             # If you use django-cors-headers
    'apps.users',              # Custom user model & JWT auth
    'apps.alerts',             # Alert logic (Celery tasks)
    'apps.analysis',           # Technical indicator calculations
    'apps.nifty_data',         # MongoDB models for stock data
]