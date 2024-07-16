from pymongo import MongoClient
from pymongo.server_api import ServerApi
import pymongo


uri = "mongodb+srv://tanams:<password>@cluster0.u98e0wd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
myclient = MongoClient(uri, server_api = ServerApi('1'))
# send a ping to confirm a successful connection
try:
    myclient.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

print(pymongo.version)


