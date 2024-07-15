from flask import Blueprint, render_template

# mainmenu blueprint definition
mainmenu = Blueprint(
    'mainmenu',
    __name__,
    static_folder='static',
    static_url_path='/pages/mainmenu',
    template_folder='templates'
)


# Routes
@mainmenu.route('/mainmenu')
def index():
    return render_template('mainmenu.html')
