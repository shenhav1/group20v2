from flask import Blueprint, render_template, session, jsonify, request, url_for
from datetime import datetime
from mongoDB import *

# contactus blueprint definition
contactus = Blueprint(
    'contactUs',
    __name__,
    static_folder='static',
    static_url_path='/pages/contactUS',
    template_folder='templates'
)


# Routes
@contactus.route('/contactus', methods=['GET', 'POST'])
def index():
    session['pagename'] = 'contactUs'
    if request.method == 'POST':
        data = request.get_json()
        if session['logged_in']:
            user = get_user_by_email(session.get('email'))
            if user:
                create_request(datetime.today().strftime('%Y-%m-%d'),
                               data.get('message'),
                               session.get('email'),
                               )
            return jsonify({'success': True, 'redirect': url_for('requestsent.index')})
        else:
            message = "You are not logged in."
            return render_template('contactUs.html', msg=message)
    return render_template('contactUs.html', msg='')
