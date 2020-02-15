from flask import Blueprint,Flask,render_template,session,request,jsonify,make_response,session
from backend.db.Groups import create_group,delete_group,query_groups
from backend.config.fields import Group_Fields
from backend.users.auth import adminRequired

meeting_blueprint = Blueprint(
    'notes_blueprint',
    __name__,
    template_folder='templates')



@meeting_blueprint.route("/")
def get_notes(): 


    return (jsonify({"success": "Return All Notes"}))

@meeting_blueprint.route("/<id>")
def get_by_id(id):
    

    return (jsonify({"success":"Return notes by ID"}))


@meeting_blueprint.route("/delete/<id>")
def remove_notes(id):


    return ({"success": "Removing notes successful!"})






