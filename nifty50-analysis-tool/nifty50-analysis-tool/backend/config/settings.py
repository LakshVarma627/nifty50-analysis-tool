import os
from pymongo import MongoClient

DATABASES = {
    'default': {
        'ENGINE': '',  # Set to an empty string or remove this line
        'NAME': os.getenv('MONGO_DB_NAME', 'nifty50'),
    }
}

mongo_client = MongoClient(os.getenv('MONGO_URI', 'mongodb://localhost:27017'))
mongo_db = mongo_client[os.getenv('MONGO_DB_NAME', 'nifty50')]