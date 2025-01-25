from datetime import datetime
from extensions import db

class Vote(db.Model):
    __tablename__ = 'votes'
    
    vote_id = db.Column(db.Integer, primary_key=True)
    fact_id = db.Column(db.Integer, db.ForeignKey('facts.fact_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    vote_type = db.Column(db.String(4), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship
    user = db.relationship('User', backref=db.backref('votes', lazy=True))
    
    __table_args__ = (
        db.UniqueConstraint('fact_id', 'user_id', name='unique_user_fact_vote'),
    )