from app import db
from datetime import datetime

class User(db.Model):
    # Primary key column
    id = db.Column(db.Integer, primary_key=True)
    
    # User identification fields
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Timestamp for record creation
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}>'
