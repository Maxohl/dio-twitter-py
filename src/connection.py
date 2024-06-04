from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client.twitter_trends

trends_collection = db.trends
