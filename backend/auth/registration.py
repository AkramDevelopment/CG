from flask import Blueprint,Flask,render_template,session,request,jsonify,make_response,session
from backend.users.auth import adminRequired
from backend.db.Accounts import Add_User,Activate_User
from backend.config.fields import Account_Fields




registeration_blueprint = Blueprint(
    'registration',
    __name__,
    template_folder='templates'
)
@registeration_blueprint.route('/register', methods=["POST"])
def createAccount():


    try:

        new_user = request.get_json(force=True)
        Add_User(new_user[Account_Fields['first-name']],new_user[Account_Fields['last-name']],new_user[Account_Fields['email']],new_user[Account_Fields['password']])
        return (jsonify({'success':"Account Created"}))


    except Exception as e :


        print(e)
        return(jsonify({"error":"There Was An Error Creating Account!"})),500





@registeration_blueprint.route("/register/activate", methods = ["PATCH"])
def activate_account():

    try:


        data = request.get_json(force = True)
        activation = Activate_User(data[Account_Fields['secondary-email']], data[Account_Fields['id']])

        if activation == False:
            return (jsonify({"error": "No Account Found with that ID!"})),404


        return (jsonify({"success!": "Account successfully updated!"}))
    except Exception as e:

        print(e)
        return ("error")


