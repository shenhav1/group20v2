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
        try:
            data = request.json  # Ensure JSON data is correctly parsed
            print(f"Form data received: {data}")  # Debug: Print form data

            if session.get('logged_in'):  # Check if the user is logged in
                user_email = session.get('email')
                user = get_user_by_email(user_email)
                if user:
                    # Debug: Print data before calling create_treatment
                    print(
                        f"Creating treatment with: address={data.get('address')}, typeOfTreatment={data.get('typeOfTreatment')}, date={data.get('date')} {data.get('time')}, therapist={data.get('therapist')}, patient={user_email}")

                    create_treatment(
                        address=data.get('address'),
                        typeOfTreatment=data.get('typeOfTreatment'),
                        date=data.get('date') + ' ' + data.get('time'),  # Combine date and time
                        therapist=data.get('therapist'),
                        patient=user_email,
                        rating=0,  # Default rating to 0
                        status='waiting approval'
                    )
                    print("Treatment successfully created.")  # Debug: Confirm treatment creation
                    return jsonify({'success': True, 'redirect': url_for('requestsent.index')})
                else:
                    message = "User not found."
                    print(message)  # Debug: User not found
                    return jsonify({'success': False, 'message': message})
            else:
                message = "You are not logged in."
                print(message)  # Debug: Not logged in
                return jsonify({'success': False, 'message': message})
        except Exception as e:
            print(f"Error processing request: {e}")  # Debug: Print any processing errors
            return jsonify({'success': False, 'message': 'Internal Server Error'}), 500
    return render_template('schedule.html', msg='', therapist=request.args.get('therapist'),
                           address=request.args.get('address'), treatment=request.args.get('treatment'))
