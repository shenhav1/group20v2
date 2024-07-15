from flask import Blueprint, render_template

# base blueprint definition
base = Blueprint(
    'base',
    __name__,
    static_folder='static',
    static_url_path='/pages/base',
    template_folder='templates'
)


# Routes
@base.route('/base')
def index():
    return render_template('base.html')
