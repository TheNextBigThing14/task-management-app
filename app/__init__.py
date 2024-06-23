# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    
    with app.app_context():
        from app import routes  # Import routes
        db.create_all()  # Create database tables for our data models
    
    return app
