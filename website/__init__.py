from flask import Flask

def create_app():
    # App config
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dad'

    from .views import views
    from .auth import auth
    from .email_service import email_service

    # Register Blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth/')
    app.register_blueprint(email_service, url_prefix='/email/')

    return app

