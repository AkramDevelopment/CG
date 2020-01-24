from flask import Blueprint,Flask,render_template,session,request,jsonify,make_response,session
from backend.db.Accounts import Query_Account_By_Email,Add_User,Query_All_Accounts,Add_Admin
from backend.users.auth import adminRequired,login_required,Developer_Required
from backend.config.fields import Account_Fields
from werkzeug.security import check_password_hash
from functools import wraps
from jwt import encode,decode

auth_blueprint = Blueprint(
    'auth',
    __name__,
    template_folder='templates'
)


@auth_blueprint.route('/register', methods = ["POST"])
def createAccount():
    try:
        new_user = request.get_json(force=True)
    
        Add_User(new_user[Account_Fields['first-name']],new_user[Account_Fields['last-name']],new_user[Account_Fields['email']],new_user[Account_Fields['password']])
        return (jsonify({'success':"Account Created"}))
    except Exception as e :
        print(e)
        return(jsonify({"error":"There Was An Error Creating Acco   unt!"})),500


@auth_blueprint.route("/login", methods = ["POST"])
def login():

    try:
        data = request.get_json(force = True)
        email = data[Account_Fields['email']]
        password = data[Account_Fields['password']]
        account = Query_Account_By_Email(email)

        if not account:
            return(jsonify({"error":"Invalid Credentials"})),401  
        if not check_password_hash(account.Password,password):


            return (jsonify({"error":"Invalid Credentials"})),401
        else:


            session.permanent = True
            token = encode({'id': account.id}, 'secret', algorithm='HS256')
            session['token'] = token
            return (jsonify({"success":"Login Successful!"}))
    except:
        return (jsonify({"error":"Not Found- User not found"}))


@auth_blueprint.route("/logout", methods = ["GET"])
def logout():

    
    session.clear()
    return(jsonify({"success":"Logout Successful"}))