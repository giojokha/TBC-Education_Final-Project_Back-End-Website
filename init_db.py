from ext import app, db
from models import  Ambavi, User


with app.app_context():
    db.drop_all()
    db.create_all()

    admin_user = User(username="admin", password="adminpass", role="Admin")
    admin_user.create()
