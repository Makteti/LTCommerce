from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///warehouse.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from .models import init_app
    init_app(app)

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
