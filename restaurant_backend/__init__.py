from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
migrate = Migrate()
manager = Manager()
ma = Marshmallow()
def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    # manager.init_app(app)

    

    with app.app_context():
        # import api blueprint from api/route.py
        from .api import routes

        # register blueprints
        app.register_blueprint(routes.api_bp)

        db.create_all()
        return app