from flask import Blueprint, render_template

# homepage blueprint definition
homepage = Blueprint(
    'homePage',
    __name__,
    static_folder='static',
    static_url_path='/pages/homePage',
    template_folder='templates'
)


# Routes
@homepage.route('/homepage')
def index():
    return render_template('homePage.html')

