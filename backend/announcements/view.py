from flask import Blueprint,Flask,request,jsonify,session
from jwt import decode
from backend.db.Accounts import Query_Account_By_ID
from backend.db.Announcements import create_announcement,query_all_announcements,query_announcement_by_id,delete_announcement
from backend.users.auth import adminRequired,login_required


announcements_blueprint = Blueprint(
    'announcements',
    __name__,
    template_folder='templates'
)

@announcements_blueprint.route('/add',methods=["POST"])
@adminRequired
def add_announcement():
    try:
        decoded = decode(session['token'],'secret',algorithms='HS256')
        created_by = Query_Account_By_ID(decoded['id'])
        print(created_by.First_Name)
        create_announcement(request.form['title'],request.form['body'],created_by.First_Name)
        return jsonify({"success":"announcement created!"})
    except:
        return jsonify({"error":"There was an error adding announcement!"}),500
    

@announcements_blueprint.route('/delete/<id>',methods = ["DELETE"])
@adminRequired
def delete_by_id(id):
    try:
        delete_announcement(id)
        return jsonify({"success":"Announcement deleted!"})
    except:
        return jsonify({"error":"There was an error deleting announcement"}),404

@announcements_blueprint.route('/view/all')
@login_required
def view_all():
   return (jsonify({"announcements":query_all_announcements()}))

@announcements_blueprint.route('/view/<id>')
@login_required
def view_by_id(id):
    try:
        announcement = query_announcement_by_id(id)
        return (jsonify({"announcement":announcement}))
    except:
        return(jsonify({"error":"Announcement with given ID not found"})),404






