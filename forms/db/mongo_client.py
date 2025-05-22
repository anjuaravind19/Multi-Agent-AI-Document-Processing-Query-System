from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

def insert_form_data(collection_name: str, data: dict):
    collection = db[collection_name]
    result = collection.insert_one(data)
    return result.inserted_id
