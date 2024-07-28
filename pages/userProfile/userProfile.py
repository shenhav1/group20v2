from flask import Blueprint, render_template, session, jsonify, redirect, url_for
from mongoDB import *

# userprofile blueprint definition
userprofile = Blueprint(
    'userprofile',
    __name__,
    static_folder='static',
    static_url_path='/pages/userprofile',
    template_folder='templates'
)


# Routes
@userprofile.route('/userprofile')
def index():
    email = session.get('email')
    if email:
        userData = get_user_by_email(email)
        user_id_str = str(userData['_id'])

        treatments = get_treatments_by_user_email_not_done(email)
        print(treatments)
        messages = get_messages_by_user_id(user_id_str)
        return render_template('userProfile.html', userData=userData, treatments=treatments, messages=messages)
    else:
        return jsonify({"error": "User not logged in"}), 401


def get_treatments_by_user_email_not_done(email):
    treatments = list(Treatment_col.find({'patient': email, 'status': {'$ne': 'done'}}))
    return treatments


@userprofile.route('/delete_treatment/<treatment_id>', methods=['POST'])
def delete_treatment(treatment_id):
    email = session.get('email')
    if email:
        print(f"Deleting treatment with ID: {treatment_id}")  # Debug line
        result = delete_treatment_by_id(treatment_id)
        print(f"Deleted count: {result.deleted_count}")  # Debug line
        return redirect(url_for('userprofile.index'))
    else:
        return jsonify({"error": "User not logged in"}), 401
