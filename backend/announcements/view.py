from flask import Blueprint,Flask,render_template,session,request,jsonify,make_response
from backend.users.auth import adminRequired,token_required



announcements_blueprint = Blueprint(
    'announcements',
    __name__,
    template_folder='templates'
)

@announcements_blueprint.route('/add')
@adminRequired
def add_announcement():
    return jsonify('Add Announcements')
    

@announcements_blueprint.route('/delete/id')
@adminRequired
def delete_by_id():
    return (jsonify("Delete By ID"))


@announcements_blueprint.route('view/all')
@token_required
def view_all():
    return (jsonify("View All By ID "))


@announcements_blueprint.route('/view/id')
@token_required
def view_by_id():
    return (jsonify("View Announcements By ID"))



