import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

# Loading environment variables from a file .env
load_dotenv()

# Getting a URI from the operating system or the cube .env
uri = os.getenv('DB_URI')
if uri is None:
    raise ValueError('DB_URI environment variable not set')

client = MongoClient(uri, server_api=ServerApi('1'))
mydatabase = client['happySoul']
customers_col = mydatabase['happySoul']


# Define collections
Users_col = mydatabase['users']
Therapist_col = mydatabase['therapist']
Treatment_col = mydatabase['Treatment']
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


#USERS
def get_user_by_email(email):
    return Users_col.find_one({'Email': email})


def check_if_signed(email):
    if get_user_by_email(email):
        return True
    return False


def create_user(email, password, first_name, last_name, city, phone_number, birthdate, entitlement):
    new_user = {
        'Email': email,
        'Password': password,
        'FirstName': first_name,
        'LastName': last_name,
        'City': city,
        'PhoneNumber': phone_number,
        'BirthDate': birthdate,
        'Entitlement': entitlement
    }
Users_col.insert_one(new_user)


