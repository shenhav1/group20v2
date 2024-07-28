from flask import Blueprint, render_template, request, jsonify
from mongoDB import ObjectId, Treatment_col

# rating blueprint definition
rating = Blueprint(
    'rating',
    __name__,
    static_folder='static',
    static_url_path='/pages/rating',
    template_folder='templates'
)

@rating.route('/rating', methods=['GET'])
def index():
    treatment_id = request.args.get('treatment_id')
    treatment_date = request.args.get('treatment_date')
    return render_template('rating.html', treatment_id=treatment_id, treatment_date=treatment_date)

@rating.route('/submit_rating', methods=['POST'])
def submit_rating():
    try:
        data = request.get_json()
        averageRating = data.get('averageRating')
        treatment_id = data.get('treatmentId')

        print(f"Received data: {data}")  # Debugging
        print(f"Treatment ID: {treatment_id}")  # Debugging

        if treatment_id:
            treatment_object_id = ObjectId(treatment_id)  # Convert to ObjectId

            # Update the treatment with the new average rating
            Treatment_col.update_one(
                {'_id': treatment_object_id},
                {'$set': {
                    'rating': averageRating
                }}
            )

            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'message': 'Treatment ID not provided'}), 400
    except Exception as e:
        print(f"Error processing rating: {e}")
        return jsonify({'success': False, 'message': 'Internal Server Error'}), 500
