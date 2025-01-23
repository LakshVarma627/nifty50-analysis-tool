import os
import requests
from pymongo import MongoClient

# MongoDB configuration
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
MONGO_DB_NAME = os.getenv('MONGO_DB_NAME', 'nifty50')
mongo_client = MongoClient(MONGO_URI)
mongo_db = mongo_client[MONGO_DB_NAME]
collection = mongo_db['stock_data']

# Function to fetch stock data from an API
def fetch_stock_data():
    api_url = "https://api.example.com/nifty50/stocks"  # Replace with actual API endpoint
    api_key = os.getenv('STOCK_API_KEY')  # Ensure this environment variable is set

    response = requests.get(api_url, headers={"Authorization": f"Bearer {api_key}"})
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

# Function to store fetched data in MongoDB
def store_stock_data(data):
    if data:
        collection.insert_many(data)
        print("Data successfully stored in MongoDB")
    else:
        print("No data to store")

if __name__ == "__main__":
    try:
        stock_data = fetch_stock_data()
        store_stock_data(stock_data)
    except Exception as e:
        print(f"An error occurred: {e}")