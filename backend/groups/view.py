from flask import Blueprint,Flask,render_template,session,request,jsonify,make_response,session
from backend.db.Groups import create_group,delete_group,query_groups
from backend.config.fields import Group_Fields
from backend.users.auth import adminRequired

groups_blueprint = Blueprint(
    'groups_blueprint',
    __name__,
    template_folder='templates')




@groups_blueprint.route("/create",methods=["POST"])
@adminRequired
def create():
    try:
        data = request.get_json(force=True)
        create_group(data[Group_Fields["group-name"]],data[Group_Fields['group-description']],data[Group_Fields['created-by']])
        return (jsonify({"success":"Event Successfully Created!"}))
    except Exception as e:

        return (jsonify({"error":e}))


@groups_blueprint.route("/delete/<id>",methods = ["DELETE"])
@adminRequired
def delete():
    try:
        delete_group(id)
        return jsonify({"success":"Group Deleted!"})
    except Exception as e:
        return (jsonify({"error": e}))


@groups_blueprint.route("/view",methods = ["GET"])
@adminRequired
def query_all():

    
    try:
        return(query_groups())
    except Exception as e:
        return (jsonify({"error":e}))


