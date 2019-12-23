from flask import Blueprint,Flask,render_template,session,request,jsonify,make_response,session
from werkzeug.security import check_password_hash
from backend.db.Accounts import Query_Account_By_Email,Add_User,Query_All_Accounts,Deactivate_Account,Add_Admin
from backend.users.auth import adminRequired,token_required,Developer_Required
from functools import wraps
from jwt import encode,decode

SESSION_COOKIE_SECURE = True
user_blueprint = Blueprint(
    'user',
    __name__,
    template_folder='templates'
)



@user_blueprint.route("/lookup/all", methods = ["GET"])
@adminRequired
def lookup():
    if len(Query_All_Accounts()) == 0:
        return (jsonify({"Message":"There Are No Accounts"}))
    return (jsonify(Query_All_Accounts()))


@user_blueprint.route("/lookup/email", methods = ["POST"])
@adminRequired
def lookupEmail():
    email = request.form["Email"]
    account = Query_Account_By_Email(email)
    if account:
        return ({'Account':{'Email': account.Email,'First_Name':account.First_Name,'Last_Name':account.Last_name ,'ID': account.id,"Position":account.Position}})
        
    else:
        return (jsonify({"Error":"There is no Account with that email"}))


@user_blueprint.route("/deactivate", methods = ["POST"])
@adminRequired
def DeactivateAccount():
    try:
        email = request.form["Email"]
        account = Query_Account_By_Email(email)
        Deactivate_Account(account.id)
        return (jsonify({"Message":"Account has been deactivated!"}))
    except:
        return (jsonify({"Error":"There was an error deactivating account!"}))


    









 