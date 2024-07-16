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



@signup.route('/signup', methods= ['GET', 'POST'])
# def index():
#    return render_template('signUp.html')
def signup():
    session['pagename'] = 'signUp'
    if request.method == 'POST':
        if not check_if_signed(request.form.get('email')):
            create_user(request.form.get('email'),
                        request.form.get('password'),
                        request.form.get('first_name'),
                        request.form.get('last_name'),
                        request.form.get('city'),
                        request.form.get('phone_number'),
                        request.form.get('birthdate'),
                        request.form.get('entitlement')
            )
            return redirect(url_for('login.login'))
        else:
            message = "This email is already signed."
            #fix css and stuff
            return render_template('signUp.html', msg=message)
    return render_template('signUp.html', msg='')

