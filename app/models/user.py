from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}>' 

<tr>
  <td>{{ user.username }}</td>
  <td>{{ user.email }}</td>
  <td>
    <form action="{{ url_for('main.delete_user', user_id=user.id) }}" method="POST" style="display:inline;">
      <button type="submit" onclick="return confirm('Are you sure you want to delete this user?');">Delete</button>
    </form>
  </td>
</tr>

