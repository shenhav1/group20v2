from flask import Blueprint, render_template, jsonify, session
from mongoDB import *

# treatmenthistory blueprint definition
treatmenthistory = Blueprint(
    'treatmenthistory',
    __name__,
    static_folder='static',
    static_url_path='/pages/treatmenthistory',
    template_folder='templates'
)


# Routes
@treatmenthistory.route('/treatmenthistory')
def index():
    email = session.get('email')
    if email:
        userData = get_user_by_email(email)

        # Retrieve treatments by user email
        treatments = get_treatments_by_user_email_done(email)
        return render_template('treatmentHistory.html', userData=userData, treatments=treatments)
    else:
        return jsonify({"error": "User not logged in"}), 401


# Sample function to retrieve treatments by user email
def get_treatments_by_user_email_done(email):
    treatments = list(Treatment_col.find({'patient': email, 'status': 'done'}))
    return treatments
