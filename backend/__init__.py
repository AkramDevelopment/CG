from datetime import timedelta
from flask import Blueprint,Flask,session
from backend.users.view import user_blueprint
from backend.announcements.view import announcements_blueprint
from backend.meeting_notes.view import meeting_blueprint
from backend.auth.registration import registeration_blueprint
from backend.auth.view import auth_blueprint
from backend.events.view import event_blueprint
from backend.groups.view import groups_blueprint
from backend.groups.roster import roster_blueprint
import os


app = Flask(__name__)



app.config["SECRET_KEY"] = os.urandom(80)
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=60)
app.register_blueprint(user_blueprint,url_prefix="/user")
app.register_blueprint(meeting_blueprint,url_prefix="/notes")
app.register_blueprint(announcements_blueprint,url_prefix="/announcements")
app.register_blueprint(auth_blueprint,url_prefix="/auth")
app.register_blueprint(registeration_blueprint,url_prefix="/auth")
app.register_blueprint(event_blueprint,url_prefix="/events")
app.register_blueprint(groups_blueprint,url_prefix="/group")
app.register_blueprint(roster_blueprint,url_prefix="/roster")



