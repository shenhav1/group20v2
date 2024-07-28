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


def get_treatments_by_user_email(email):
    return list(mydatabase.Treatment_col.find({'userEmail': email, 'status': {'$ne': 'Done'}}))


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

def get_treatments_by_user_email_done(email):
        try:
            treatments = Treatment_col.find({'patient': email, 'status': 'done'})
            treatments_list = list(treatments)
            if treatments_list:
                print(f"Treatments found: {treatments_list}")  # Debugging statement
            else:
                print("No treatments found")  # Debugging statement
            return treatments_list
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
        # Create a case-insensitive regular expression to match part of the name
        query = {'name': {'$regex': name, '$options': 'i'}}
        therapist = Therapist_col.find_one(query)
        if therapist:
            print(f"Therapist found: {therapist}")  # Debugging statement
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


def get_therapist_by_fields(search_by_name=None, treatment_type=None, city=None, therapist_gender=None,
                            entitlement=None):
    query = {}
    if treatment_type:
        query['proposedTreatments'] = treatment_type
    if entitlement:
        query['entitlement'] = entitlement
    if therapist_gender:
        query['gender'] = therapist_gender
    if city:
        query['clinicLocation'] = {'$regex': city, '$options': 'i'}

    try:
        therapists = list(Therapist_col.find(query))

        if search_by_name:
            therapists = [
                therapist for therapist in therapists
                if search_by_name.lower() in therapist['name'].lower()
            ]

        # Convert ObjectIds to strings
        for therapist in therapists:
            therapist['_id'] = str(therapist['_id'])

        return therapists
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def create_treatment(address, typeOfTreatment, date, therapist, patient, rating, status):
    new_treatment = {
        'address': address,
        'typeOfTreatment': typeOfTreatment,
        'date': date,
        'therapist': therapist,
        'patient': patient,
        'rating': rating,
        'status': status
    }

    try:
        result = Treatment_col.insert_one(new_treatment)
        print(f"Inserted treatment with id: {result.inserted_id}")  # Debug: Confirm insertion
    except Exception as e:
        print(f"Error inserting treatment: {e}")  # Debug: Print any insertion errors


def get_treatments_by_user_email_and_date_done(email, date):
    treatments = Treatment_col.find({
        'patient': email,
        'status': 'done',
        'date': date
    })
    return list(treatments)


def delete_treatment_by_id(treatment_id):
    try:
        result = mydatabase.Treatment_col.delete_one({'_id': ObjectId(treatment_id)})
        print(f"Deleted count: {result.deleted_count}")  # Debug line to check if deletion was successful
        return result
    except Exception as e:
        print(f"Error deleting treatment: {e}")
        return None

