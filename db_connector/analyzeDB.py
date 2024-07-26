import os
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from mongoDB import (get_users, get_request, get_treatment, get_message, get_therapist)
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv('DB_URI')
print(uri)
if uri is None:
    raise ValueError('DB_URI environment variable not set')

# create cluster

# get all dbs and collestions that needed
client = MongoClient(uri, server_api=ServerApi('1'))
mydatabase = client['happySoul']
# create all necessary functions

requests = get_request()
users = get_users()
messages = get_message()
therapists = get_therapist()
treatment = get_treatment()

Users_col = mydatabase['users']
Therapist_col = mydatabase['therapist']
Treatment_col = mydatabase['treatment']
request_col = mydatabase['request']
message_col = mydatabase['message']


def get_all_users():
    users = list(Users_col.find())
    print(users)


def get_all_therapists():
    therapists = list(Therapist_col.find())
    print(therapists)


def get_all_treatments():
    treatments = list(Treatment_col.find())
    print(treatments)


def get_all_requests():
    requests = list(request_col.find())
    print(requests)


def get_all_messages():
    messages = list(message_col.find())
    print(messages)


def print_all_collections():
    print("Users Collection:")
    get_all_users()
    print("\nTherapists Collection:")
    get_all_therapists()
    print("\nTreatments Collection:")
    get_all_treatments()
    print("\nRequests Collection:")
    get_all_requests()
    print("\nMessages Collection:")
    get_all_messages()


# Example usage
print_all_collections()


