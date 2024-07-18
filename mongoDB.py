import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from bson import ObjectId


# Load environment variables from a .env file
load_dotenv()

# Get the URI from the environment variables
uri = os.getenv('DB_URI')
if uri is None:
    raise ValueError('DB_URI environment variable not set')

client = MongoClient(uri, server_api=ServerApi('1'))
mydatabase = client['happySoul']
customers_col = mydatabase['happySoul']

# Define collections
Users_col = mydatabase['users']
Therapist_col = mydatabase['therapist']
Treatment_col = mydatabase['treatment']
request_col = mydatabase['request']
message_col = mydatabase['message']


def get_users():
    return mydatabase['users']


def get_request():
    return mydatabase['request']


def get_therapist():
    return mydatabase['therapist']


def get_treatment():
    return mydatabase['treatment']


def get_message():
    return mydatabase['message']


# USERS
def get_user_by_email(email):
    try:
        user = Users_col.find_one({'email': email})
        if user:
            print(f"User found: {user}")  # Debugging statement
        else:
            print("User not found")  # Debugging statement
        return user
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def check_if_signed(email):
    return get_user_by_email(email) is not None


def get_treatments():
    try:
        treatments = Treatment_col.find()
        treatments_list = list(treatments)
        if treatments_list:
            print(f"Treatments found: {treatments_list}")  # Debugging statement
        else:
            print("No treatments found")  # Debugging statement
        return treatments_list
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def get_treatments_by_user_id_not_done(userId):
    try:
        objectId = ObjectId(userId)
        treatments = Treatment_col.find({'patient': objectId, 'status': {'$ne': 'done'}})
        treatments_list = list(treatments)
        if treatments_list:
            print(f"Treatments found: {treatments_list}")  # Debugging statement
        else:
            print("No treatments found")  # Debugging statement
        return treatments_list
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def get_treatments_by_user_id_done(userId):
    try:
        objectId = ObjectId(userId)
        treatments = Treatment_col.find({'patient': objectId, 'status': 'done'})
        treatments_list = list(treatments)
        if treatments_list:
            print(f"Treatments found: {treatments_list}")  # Debugging statement
        else:
            print("No treatments found")  # Debugging statement
        return treatments_list
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def get_messages_by_user_id(userId):
    try:
        objectId = ObjectId(userId)
        messages = message_col.find({'patient': objectId})
        messages_list = list(messages)
        if messages_list:
            print(f"Messages found: {messages_list}")  # Debugging statement
        else:
            print("No messages found")  # Debugging statement
        return messages_list
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def create_user(email, password, first_name, last_name, city, phone_number, birthdate, entitlement):
    new_user = {
        'email': email,
        'password': password,
        'firstName': first_name,
        'lastName': last_name,
        'city': city,
        'cellPhoneNumber': phone_number,
        'dateOfBirth': birthdate,
        'entitlement': entitlement
    }
    Users_col.insert_one(new_user)

def get_therapist_by_name(name):
        try:
            therapist = Therapist_col.find_one({'name': name})
            if therapist:
                print("Therapist found: {therapist}")  # Debugging statement
            else:
                print(f"Therapist not found")  # Debugging statement
            return therapist
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


def create_request(date, referralContent, patient):
    new_request = {
        'date': date,
        'referralContent': referralContent,
        'patient': patient
    }
    request_col.insert_one(new_request)

def create_treatment(adress, typeOfTreatment, date, therapist, patient, rating, status):
    new_treatment = {
        'adress': adress,
        'typeOfTreatment': typeOfTreatment,
        'date': date,
        'therapist': therapist,
        'patient': patient,
        'rating': rating,
        'status': status
    }
    Treatment_col.insert_one(new_treatment)