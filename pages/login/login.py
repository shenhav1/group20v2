from flask import Blueprint, render_template, session, redirect, url_for, flash, request
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
@login.route('/login', methods = ['GET' , ' POST'])
def login():
    session['pagename'] = 'login'
    if request.method == 'POST':
        if check_if_signed(request.form.get('email')):
            user = get_user_by_email(request.form.get('email'))
            if user['Password'] == request.form.get('password'):
                session['email'] = request.form.get('email')
                session['users_name'] = user['FirstName']
                session['logged_in'] = True
                return redirect(url_for('userProfile.userprofile'))
            else:
                msg = 'Incorrect password, Please try again'
                return render_template("login.html", msg=msg)
        else:
            msg = 'Incorrect email, Please try again'
            return render_template("login.html", msg=msg)

    return render_template("login.html", msg="")

