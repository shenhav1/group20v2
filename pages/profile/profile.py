from flask import Blueprint, render_template, session, jsonify
from mongoDB import *

# profile blueprint definition
profile = Blueprint(
    'profile',
    __name__,
    static_folder='static',
    static_url_path='/pages/profile',
    template_folder='templates'
)


# Routes
@profile.route('/profile')
def index():
    name = session.get('name')
    if name:
        therapistData = get_therapist_by_name(name)

        return render_template('profile.html', therapistData=therapistData)
    else:
        return jsonify({"error": "therapist not found"}), 401
