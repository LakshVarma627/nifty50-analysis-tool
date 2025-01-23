import os
from pymongo import MongoClient

class NiftyData:
    def __init__(self):
        self.client = MongoClient(os.getenv('MONGO_URI', 'mongodb://localhost:27017'))
        self.db = self.client[os.getenv('MONGO_DB_NAME', 'nifty50')]
        self.collection = self.db['nifty_data']

    def insert_data(self, data):
        self.collection.insert_one(data)

    def get_data(self, query):
        return self.collection.find(query)
