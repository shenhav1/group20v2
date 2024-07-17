import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

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
