
from flask import Blueprint,Flask,render_template,session,request,jsonify,make_response,session
from backend.db.Accounts import get_groups
from backend.db.Roster import add_member
from backend.config.fields import Group_Fields
from backend.users.auth import adminRequired



roster_blueprint = Blueprint(
    'roster_blueprint',
    __name__,
    template_folder='templates')




@roster_blueprint.route("/view/<id>")
def get_group(id):
    groups = get_groups(id)
    

    if not groups:
        print(groups)
        return (jsonify({"groups": "There are no groups associated with this account!"}))
    else:
        return (jsonify({"groups":groups}))
       


