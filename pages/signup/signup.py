from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from mongoDB import *

# signup blueprint definition
signup = Blueprint(
    'signup',
    __name__,
    static_folder='static',
    static_url_path='/pages/signup',
    template_folder='templates'
)


@signup.route('/signup', methods=['GET', 'POST'])
def index():
    session['pagename'] = 'signUp'
    if request.method == 'POST':
        data = request.get_json()
        if not check_if_signed(data.get('email')):
            create_user(data.get('email'),
                        data.get('password'),
                        data.get('firstName'),
                        data.get('lastName'),
                        data.get('city'),
                        data.get('phoneNumber'),
                        data.get('dob'),
                        data.get('entitlement')
                        )
            return jsonify({'success': True, 'redirect': url_for('login.index')})
        else:
            message = "This email is already signed."
            # fix css and stuff
            return render_template('signUp.html', msg=message)
    return render_template('signUp.html', msg='')
