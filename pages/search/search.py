from flask import Blueprint, render_template, request, jsonify, url_for, session
from mongoDB import get_therapist_by_fields

# search blueprint definition
search = Blueprint(
    'search',
    __name__,
    static_folder='static',
    static_url_path='/pages/search',
    template_folder='templates'
)

# Routes
@search.route('/search', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        search_by_name = data.get('searchByName')
        treatment_type = data.get('treatmentType')
        city = data.get('city')
        therapist_gender = data.get('therapistGender')
        entitlement = data.get('entitlement')

        therapists = get_therapist_by_fields(
            search_by_name=search_by_name,
            treatment_type=treatment_type,
            city=city,
            therapist_gender=therapist_gender,
            entitlement=entitlement
        )

        # Store the search results in the session
        session['search_results'] = therapists
        return jsonify({'redirect': url_for('searchResult.index')})
    else:
        return render_template('search.html')
