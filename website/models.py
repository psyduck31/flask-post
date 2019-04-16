from website import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
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
