from flask import Blueprint, render_template

# profile blueprint definition
profile = Blueprint(
    'profile',
    __name__,
    static_folder='static',
    static_url_path='/pages/profile',
    template_folder='templates'
)


# Routes
@profile.route('/profile')
def index():
    return render_template('profile.html')
