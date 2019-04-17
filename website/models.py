from website import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return f"User('{self.id}', '{self.username}')"


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(20), nullable = False)
    text = db.Column(db.String(255), nullable = False)
    author_name = db.Column(db.String(20), nullable = False)
    author_id = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"Posts('{self.id}','{self.author_name}','{self.author_id}', '{self.title}', '{self.text}')"
