from flask import Blueprint, render_template

# search blueprint definition
search = Blueprint(
    'search',
    __name__,
    static_folder='static',
    static_url_path='/pages/search',
    template_folder='templates'
)


# Routes
@search.route('/search')
def index():
    return render_template('search.html')
