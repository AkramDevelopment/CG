from flask import Blueprint,Flask
from backend.users.view import user_blueprint
from backend.announcements.view import announcements_blueprint


app = Flask(__name__)



app.config["SECRET_KEY"] = "PLACEHOLDER"
app.register_blueprint(user_blueprint,url_prefix="/user")
app.register_blueprint(announcements_blueprint,url_prefix="/announcements")