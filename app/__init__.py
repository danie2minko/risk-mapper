from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Initialisation des extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    """
    Factory pour créer et configurer l'instance de l'application Flask.
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)
    
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Lier les extensions à l'instance de l'application
    db.init_app(app)
    # L'astuce : passer les modèles directement à Migrate ici
    from app import models
    migrate.init_app(app, db)

    # Importer et enregistrer les blueprints (nos routes)
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app