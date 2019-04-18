from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.mock_api_server