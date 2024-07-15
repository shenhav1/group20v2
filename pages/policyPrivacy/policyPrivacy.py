from flask import Blueprint, render_template

# policyprivacy blueprint definition
policyprivacy = Blueprint(
    'policyPrivacy',
    __name__,
    static_folder='static',
    static_url_path='/pages/policyPrivacy',
    template_folder='templates'
)


# Routes
@policyprivacy.route('/policyprivacy')
def index():
    return render_template('policyPrivacy.html')
