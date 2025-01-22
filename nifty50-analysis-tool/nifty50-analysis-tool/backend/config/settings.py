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
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    # 'django.contrib.sessions',
    'your_app',
]