from flask import Blueprint, render_template

# treatmenthistory blueprint definition
treatmenthistory = Blueprint(
    'treatmenthistory',
    __name__,
    static_folder='static',
    static_url_path='/pages/treatmenthistory',
    template_folder='templates'
)


# Routes
@treatmenthistory.route('/treatmenthistory')
def index():
    return render_template('treatmentHistory.html')
