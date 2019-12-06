from flask import Blueprint,Flask
from backend.users.view import user_blueprint


app = Flask(__name__)



app.config["SECRET_KEY"] = "PLACEHOLDER"
app.register_blueprint(user_blueprint,url_prefix="/user")