import os
from pymongo import MongoClient

mongo_uri = os.environ.get("MONGO_URI", "mongodb://localhost:27017/campus_app")
client = MongoClient(mongo_uri)
db = client["campus_app"] 