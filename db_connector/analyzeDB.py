import os
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from mongoDB import ( get_users , get_request , get_treatment, get_message, get_therapist)


# get your uri from .env file
uri = os.environ.get('DB_URI')

if uri is None:
    raise ValueError('DB_URI environment variable not set')

# create cluster
cluster = MongoClient(uri, server_api=ServerApi('1'))

# get all dbs and collestions that needed
mydatabase = cluster['mydatabase']


# create all necessary functions

requests = get_request()
users = get_users()
messages = get_message()
therapists = get_therapist()
treatment = get_treatment()
