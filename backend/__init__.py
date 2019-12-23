from datetime import timedelta
from flask import Blueprint,Flask,session
from backend.users.view import user_blueprint
from backend.announcements.view import announcements_blueprint
from backend.auth.view import auth_blueprint


app = Flask(__name__)



app.config["SECRET_KEY"] = "PLACEHOLDER"
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=60)
app.register_blueprint(user_blueprint,url_prefix="/user")
app.register_blueprint(announcements_blueprint,url_prefix="/announcements")
app.register_blueprint(auth_blueprint,url_prefix="/auth")