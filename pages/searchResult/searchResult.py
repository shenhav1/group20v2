from flask import Blueprint, render_template

# searchresult blueprint definition
searchresult = Blueprint(
    'searchResult',
    __name__,
    static_folder='static',
    static_url_path='/pages/searchResult',
    template_folder='templates'
)


# Routes
@searchresult.route('/searchresult')
def index():
    return render_template('searchResult.html')
