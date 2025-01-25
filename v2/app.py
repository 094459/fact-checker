from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from extensions import db, login_manager

def create_app():
    app = Flask(__name__)
    
    # Configure the Flask app
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///factcheck.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        # Note: user_id is a string, so we need to convert it to int
        return User.query.get(int(user_id))
        
    with app.app_context():
        # Import and register blueprints
        from routes.auth import auth_bp
        from routes.main import main_bp
        
        app.register_blueprint(auth_bp)
        app.register_blueprint(main_bp)
        
        # Create database tables
        db.create_all()
        
        return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)