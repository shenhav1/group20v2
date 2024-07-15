from flask import Flask

###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## base
from pages.base.base import base

app.register_blueprint(base)
## Homepage
from pages.homePage.homePage import homepage

app.register_blueprint(homepage)
## Signup
from pages.signup.signup import signup

app.register_blueprint(signup)
## contactTherapist
from pages.contactTherapist.contactTherapist import contacttherapist

app.register_blueprint(contacttherapist)
## contactUs
from pages.contactUs.contactUs import contactus

app.register_blueprint(contactus)
## login
from pages.login.login import login

app.register_blueprint(login)
## userprofile
from pages.userProfile.userProfile import userprofile

app.register_blueprint(userprofile)
## treatmenthistory
from pages.treatmentHistory.treatmentHistory import treatmenthistory

app.register_blueprint(treatmenthistory)
## rating
from pages.rating.rating import rating

app.register_blueprint(rating)
## requestsent
from pages.requestSent.requestSent import requestsent

app.register_blueprint(requestsent)
## policyprivacy
from pages.policyPrivacy.policyPrivacy import policyprivacy

app.register_blueprint(policyprivacy)
## profile
from pages.profile.profile import profile

app.register_blueprint(profile)
## schedule
from pages.schedule.schedule import schedule

app.register_blueprint(schedule)
## searchresult
from pages.searchResult.searchResult import searchresult

app.register_blueprint(searchresult)
## search
from pages.search.search import search

app.register_blueprint(search)
##mainmenu
from components.main_menu.mainmenu import mainmenu

app.register_blueprint(mainmenu)
# from pages.menu.menu import menu
#
# app.register_blueprint(menu)
#
# ## Catalog
# from pages.catalog.catalog import catalog
#
# app.register_blueprint(catalog)
#
# ## Page error handlers
# from pages.page_error_handlers.page_error_handlers import page_error_handlers
#
# app.register_blueprint(page_error_handlers)
#
# ###### Components
# ## Main menu
# from components.main_menu.main_menu import main_menu
#
# app.register_blueprint(main_menu)

if __name__ == '__main__':
    app.run(debug=True)