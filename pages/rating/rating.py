from flask import Blueprint, render_template

# rating blueprint definition
rating = Blueprint(
    'rating',
    __name__,
    static_folder='static',
    static_url_path='/pages/rating',
    template_folder='templates'
)


# Routes
@rating.route('/rating')
def index():
    return render_template('rating.html')
