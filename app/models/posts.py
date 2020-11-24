from app.extensions._db import db


class PostsModel(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), unique=True, nullable=False)
    title = db.Column(db.String(128), nullable=False)
    post = db.Column(db.Text, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)


    def __repr(self):
        return f"<Posts {self.full_name}>"