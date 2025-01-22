import os
from pymongo import MongoClient

DATABASES = {}

mongo_client = MongoClient(os.getenv('MONGO_URI', 'mongodb+srv://lakshvarma6:your_password@nifty-mongo.5ztn7.mongodb.net/?retryWrites=true&w=majority&appName=nifty-mongo'))
mongo_db = mongo_client[os.getenv('MONGO_DB_NAME', 'nifty50')]