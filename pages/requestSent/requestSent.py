from flask import Blueprint, render_template

# requestsent blueprint definition
requestsent = Blueprint(
    'requestsent',
    __name__,
    static_folder='static',
    static_url_path='/pages/requestSent',
    template_folder='templates'
)


# Routes
@requestsent.route('/requestsent')
def index():
    return render_template('requestSent.html')
