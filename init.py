from flask import Flask
from app.config import Config
from app.models import db, bcrypt, jwt
from app.routes import bp as main_bp
from app.auth import auth as auth_bp
from app.reports import reports as reports_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(reports_bp)

    with app.app_context():
        db.create_all()

    return app
