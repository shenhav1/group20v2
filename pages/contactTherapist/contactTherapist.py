from flask import Blueprint, render_template

# contacttherapist blueprint definition
contacttherapist = Blueprint(
    'contactTherapist',
    __name__,
    static_folder='static',
    static_url_path='/pages/contactTherapist',
    template_folder='templates'
)


# Routes
@contacttherapist.route('/contacttherapist')
def index():
    return render_template('contactTherapist.html')
