from extensions import db
from datetime import datetime

class Category(db.Model):
    __tablename__ = 'categories'
    
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    
    facts = db.relationship('Fact', backref='category', lazy=True)

class Fact(db.Model):
    __tablename__ = 'facts'
    
    fact_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'), nullable=False)
    fact_text = db.Column(db.Text, nullable=False)
    supporting_url = db.Column(db.Text)
    supporting_info = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, server_default=db.func.current_timestamp(), onupdate=datetime.utcnow)
    
    votes = db.relationship('Vote', backref='fact', lazy=True)

class Vote(db.Model):
    __tablename__ = 'votes'
    
    vote_id = db.Column(db.Integer, primary_key=True)
    fact_id = db.Column(db.Integer, db.ForeignKey('facts.fact_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    is_true = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())