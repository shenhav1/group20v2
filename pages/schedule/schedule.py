from flask import Blueprint, render_template, session, jsonify, request, url_for
from mongoDB import *

# schedule blueprint definition
schedule = Blueprint(
    'schedule',
    __name__,
    static_folder='static',
    static_url_path='/pages/schedule',
    template_folder='templates'
)


# Routes
@schedule.route('/schedule', methods=['GET', 'POST'])
def index():
    session['pagename'] = 'schedule'
    if request.method == 'POST':
        data = request.get_json()
        if session.get('logged_in'):  # Check if the user is logged in
            user = get_user_by_email(session.get('email'))
            create_treatment(data.get('address'),
                                 data.get('typeOfTreatment'),
                                 data.get('date'),
                                 data.get('therapist'),
                                 session.get('email'),
                                 data.get('rating'),
                                 'waiting approval')
            return jsonify({'success': True, 'redirect': url_for('requestsent')})
        else:
            message = "you are not logged in."
            return render_template('schedule.html', msg=message)
    return render_template('schedule.html', msg='')