
from flask import Blueprint,Flask,render_template,session,request,jsonify,make_response,session
from backend.db.Groups import create_group,delete_group,query_groups
from backend.config.fields import Group_Fields
from backend.users.auth import adminRequired




roster_blueprint = Blueprint(
    'roster_blueprint',
    __name__,
    template_folder='templates')



#Query groups that account is in

#Query all group rosters

