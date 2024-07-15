from pymongo import MongoClient

# Replace 'mongodb://localhost:27017/' with your MongoDB connection string
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']  # Replace with your database name
collection = db['users']  # Replace with your collection name
