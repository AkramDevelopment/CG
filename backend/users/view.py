from flask import Blueprint,Flask,render_template,session,request,jsonify,make_response
from werkzeug.security import check_password_hash
from backend.db.Accounts import Query_Account_By_Email,Add_User
from backend.users.auth import adminRequired,token_required
from functools import wraps
from jwt import encode,decode


user_blueprint = Blueprint(
    'user',
    __name__,
    template_folder='templates'
)

@user_blueprint.route('/register', methods = ["POST"])
def createAccount():
    new_user =  {"First_Name":request.form["First_Name"],"Last_Name":request.form["Last_Name"],"Email":request.form["Email"],"Password":request.form["Password"]}
    if Query_Account_By_Email(new_user["Email"]):
        return ("There Is Already An Account Associated With that Email!")
    Add_User(new_user["First_Name"],new_user["Last_Name"],new_user["Email"],new_user["Password"])
    return ("Account Created")

@user_blueprint.route("/auth/login", methods = ["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]

    account = Query_Account_By_Email(email)
    if not account:
        return("There is no account with those credentials")  
    if not check_password_hash(account.Password,password):
        return ("Invalid Credentials")
    else:
        token = encode({'id': account.id}, 'secret', algorithm='HS256')
        return (token)


@user_blueprint.route("/test", methods = ["POST"])
def test():
    email = request.form["Email"]
    password = request.form["Password"]

    account = Query_Account_By_Email(email)
    if not account:
        return("There is no account with those credentials")  
    if not check_password_hash(account.Password,password):
        return ("Invalid Credentials")
    
    token = encode({'id': account.id}, 'secret', algorithm='HS256')
    resp = make_response('Setting Cookie!')
    resp.set_cookie('token','token')
    return (token)
