from datetime import datetime
from extensions import db

class Fact(db.Model):
    __tablename__ = 'facts'
    
    fact_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    supporting_url = db.Column(db.Text)
    supporting_info = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    user = db.relationship('User', backref=db.backref('facts', lazy=True))
    category = db.relationship('Category', backref=db.backref('facts', lazy=True))
    votes = db.relationship('Vote', backref='fact', lazy=True)