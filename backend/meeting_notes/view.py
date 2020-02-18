from flask import Blueprint,Flask,render_template,session,request,jsonify,make_response,session
from backend.db.Meeting_Notes import create_notes,query_all,query_by_id
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
    try:

        result = query_by_id(id)
        return (jsonify(result))
    
    except:

        return (jsonify({"success":"Return notes by ID"}))


@meeting_blueprint.route("/delete/<id>")
def remove_notes(id):


    return ({"success": "Removing notes successful!"})






