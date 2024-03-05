from flask import Flask
from .views.home import home
from .views.about import about
from .views.recognition import recognition
from .views.dashbord import dashboard
from .views.sign_in import sign_in
from .views.sign_out import sign_out


def create_app():

    app = Flask(__name__)
    app.register_blueprint(home, url_prefix="/")
    app.register_blueprint(about, url_prefix="/about")
    app.register_blueprint(recognition, url_prefix="/recognition")
    app.register_blueprint(dashboard, url_prefix="/dashboard")
    app.register_blueprint(sign_in, url_prefix="/sign-in")
    app.register_blueprint(sign_out, url_prefix="/sign-out")

    return app
