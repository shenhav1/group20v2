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
def index():
    return render_template('userProfile.html')