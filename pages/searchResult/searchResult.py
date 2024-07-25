from flask import Blueprint, render_template, session, request

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
    # Retrieve search results from the session
    search_results = session.get('search_results', [])
    return render_template('searchResult.html', therapists=search_results)

@searchresult.route('/set_therapist_name', methods=['POST'])
def set_therapist_name():
    data = request.get_json()
    session['name'] = data.get('name')
    return '', 204  # No Content response