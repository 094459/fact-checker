from datetime import datetime
from app import db

class Fact(db.Model):
    __tablename__ = 'facts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Relationships
    votes = db.relationship('Vote', backref='fact', lazy=True)

class Category(db.Model):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    
    # Relationships
    facts = db.relationship('Fact', backref='category', lazy=True)

class Vote(db.Model):
    __tablename__ = 'votes'
    
    id = db.Column(db.Integer, primary_key=True)
    is_fact = db.Column(db.Boolean, nullable=False)
    supporting_info = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    fact_id = db.Column(db.Integer, db.ForeignKey('facts.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)