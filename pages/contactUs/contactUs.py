from flask import Blueprint, render_template

# contactus blueprint definition
contactus = Blueprint(
    'contactUs',
    __name__,
    static_folder='static',
    static_url_path='/pages/contactUS',
    template_folder='templates'
)


# Routes
@contactus.route('/contactus')
def index():
    return render_template('contactUs.html')
