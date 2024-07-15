from flask import Blueprint, render_template, request, redirect, url_for

# signup blueprint definition
signup = Blueprint(
    'signup',
    __name__,
    static_folder='static',
    static_url_path='/pages/signup',
    template_folder='templates'
)

@signup.route('/signup', methods=['GET', 'POST'])
# def index():
#     return render_template('signUp.html')
def signup(session=None, user_col=None):
    if request.method == 'GET':
        return render_template('signUp.html')
    elif request.method == 'POST':
        print("post is activated")

        # Process user registration using data from the form
        email = request.form.get("email")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        password = request.form.get("password")
        city = request.form.get("city")
        phone_number = request.form.get("phone_number")
        birthday = request.form.get("birthday")
        entitlement = request.form.get("entitlement")


        existing_user = user_col.find_one({'Email': email})
        print(email)
        if existing_user:
            print(f"Error: User with email {email} already exists. Please choose a different email.")
            return render_template('signUp.html',
                                   message="User already exists with this email. Please choose a different email.")
        else:
            # Create a new user and insert it into the 'users' collection
            new_user = {
                'email': email,
                'first name': first_name,
                'last name': last_name,
                'password': password,
                'city': city,
                'phone number': phone_number,
                'birthday': birthday,
                'entitlement': entitlement
            }

            user_col.insert_one(new_user)
            session['email'] = email
            session['first_name'] = first_name
            session['last_name'] = last_name
            session['phone_number'] = phone_number
            session['city'] = city
            session['entitlement']: entitlement

            print(f"Account for {email} created successfully.")
            return redirect(url_for('login'))