
from flask import Blueprint,Flask,render_template,session,request,jsonify,make_response,session
from backend.db.Accounts import get_groups
from backend.db.Roster import add_member,add_admin,remove_admin
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


        
        return (jsonify({"groups": "There are no groups associated with this account!"}))
    else:

        
        return (jsonify({"groups":groups}))
       



@roster_blueprint.route("/add/admin/<account_id>/<group_id>", methods = ["PATCH"])
def Add_Admin(account_id,group_id):
    try:

        #Create route to give a member admin access to a specific group
        if add_admin(account_id,group_id) == True:
            return (jsonify({"success": " Account has been made an admin for group successfully!"}))
        else:


            return (jsonify({"error":"There was a error adding user as an admin, group or user not found!"})),404
    except Exception as e:


        print(e)
        return (jsonify({"error":"There was an internal error when adding admin"})),500


@roster_blueprint.route("/remove/admin/<account_id>/<group_id>",methods = ["PATCH"])
def Remove_Admin(account_id,group_id):

    try:

        if remove_admin(account_id,group_id) == True:
            return (jsonify({"success": "Admin for group removed!"}))
        else:
            return (jsonify({"error": "Account or group no found!"})),404
    except Exception as e:
        print(e)
        return (jsonify({"error":"There was an internal server error"})),500



