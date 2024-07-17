from flask import Blueprint, render_template, session, redirect, url_for, flash, request, jsonify
from mongoDB import *

# login blueprint definition
login = Blueprint(
    'login',
    __name__,
    static_folder='static',
    static_url_path='/pages/login',
    template_folder='templates'
)

# Routes
@login.route('/login', methods=['GET', 'POST'])
def index():
    session['pagename'] = 'login'
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        if check_if_signed(email):
            user = get_user_by_email(email)
            if user['password'] == password:
                session['email'] = email
                session['users_name'] = user['firstName']
                session['logged_in'] = True
                return jsonify({'success': True, 'redirect': url_for('userprofile.index')})
            else:
                return jsonify({'success': False, 'message': 'Incorrect password, Please try again'})
        else:
            return jsonify({'success': False, 'message': 'Incorrect email, Please try again'})

    return render_template("login.html", msg="")