from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'speed run'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5432/diseases'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #postgresql://postgres:12345@localhost:5432/diseases
    db.init_app(app)

    from .views import views
    from .crud import crud

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(crud, url_prefix='/')

    from .models import Record
    
    return app