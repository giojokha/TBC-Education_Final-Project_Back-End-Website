from ext import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class BaseModel:
    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def save():
        db.session.commit()


class Ambavi(db.Model, BaseModel):
    __tablename__ = "Ambebi"

    id = db.Column(db.Integer(), primary_key=True)
    Date = db.Column(db.Integer(), nullable=False)
    news_title = db.Column(db.String(), nullable=False)
    image = db.Column(db.String(), default="default_name.png")

class User(db.Model, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    role = db.Column(db.String())

    def __init__(self, username, password, role="Guest"):
        self.username = username
        self.password = generate_password_hash(password)
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password, password)  # True or False


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)