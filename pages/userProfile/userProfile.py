from flask import Blueprint, render_template

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
def show_messages():
    # Query the database to get messages
    messages = messages_col.find().sort('_id', -1)

    return render_template('userProfile.html', messages=messages)