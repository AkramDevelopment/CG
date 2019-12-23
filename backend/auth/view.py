from flask import Blueprint,Flask,render_template,session,request,jsonify,make_response,session
from werkzeug.security import check_password_hash
from backend.db.Accounts import Query_Account_By_Email,Add_User,Query_All_Accounts,Deactivate_Account,Add_Admin
from backend.users.auth import adminRequired,token_required,Developer_Required
from functools import wraps
from jwt import encode,decode

auth_blueprint = Blueprint(
    'auth',
    __name__,
    template_folder='templates'
)


@auth_blueprint.route('/register', methods = ["POST"])
def createAccount():
    new_user =  {"First_Name":request.form["First_Name"],"Last_Name":request.form["Last_Name"],"Email":request.form["Email"],"Password":request.form["Password"]}
  
    Add_User(new_user["First_Name"],new_user["Last_Name"],new_user["Email"],new_user["Password"])
    return ("Account Created")


@auth_blueprint.route("/login", methods = ["POST"])
def login():
    
    email = request.form["Email"]
    password = request.form["Password"]

    account = Query_Account_By_Email(email)
    if not account:
        return(jsonify({"error":"Invalid Credentials"}))  
    if not check_password_hash(account.Password,password):
        return (jsonify({"error":"Invalid Credentials"}))
    else:
        session.permanent = True
        token = encode({'id': account.id}, 'secret', algorithm='HS256')
        session['token'] = token
        return (jsonify({"success":"Login Successful!"}))
        

@auth_blueprint.route("/logout", methods = ["GET"])
def logout():
    session.clear()
    return(jsonify({"success":"Logout Successful"}))