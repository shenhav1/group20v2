from flask import Blueprint, render_template, request, jsonify
from mongoDB import *
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
    if request.method == 'POST':
        data = request.get_json()
        formData = data.get('formData')
        averageRating = data.get('averageRating')

        # Assuming you have the treatment_id from the session or request
        treatment_id = request.args.get('treatment_id')  # Or retrieve it from session or other source

        if treatment_id:
            treatment_object_id = ObjectId(treatment_id)  # Convert to ObjectId

            # Update the treatment with the new rating and average rating
            Treatment_col.update_one(
                {'_id': treatment_object_id},
                {'$set': {
                    'therapistRating': formData['therapistRating'],
                    'clinicRating': formData['clinicRating'],
                    'treatmentHelp': formData['treatmentHelp'],
                    'generalRating': formData['generalRating'],
                    'comments': formData['comments'],
                    'averageRating': averageRating
                }}
            )

            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'message': 'Treatment ID not provided'}), 400
    return render_template('rating.html')

