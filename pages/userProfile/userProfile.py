from flask import Blueprint, render_template, session, jsonify
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
        print(user_id_str)
        treatments = get_treatments_by_user_id_not_done(user_id_str)
        return render_template('userProfile.html', userData=userData, treatments=treatments)
    else:
        return jsonify({"error": "User not logged in"}), 401