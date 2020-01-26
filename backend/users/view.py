from backend.db.Accounts import Query_Account_By_Email,Add_User,Query_All_Accounts,Add_Admin,Query_Roster,Is_Admin,Query_Account_By_ID,Get_Inactives
from flask import Blueprint,Flask,render_template,session,request,jsonify,make_response,session
from backend.users.auth import adminRequired,login_required,Developer_Required,check_admin
from backend.db.Banned_Accounts import ban_account,unban_account
from werkzeug.security import check_password_hash
from backend.users.sessions import get_session_id
from backend.logging.loggers import log_unban
from jwt import encode,decode


SESSION_COOKIE_SECURE = True
user_blueprint = Blueprint(
    'user',
    __name__,
    template_folder='templates'
)


@user_blueprint.route("/isadmin")
@check_admin
def check_admin_test():


    return(jsonify({"response":"Check Admin Route"}))
        


@user_blueprint.route("/lookup/all", methods = ["GET"])
@adminRequired
def lookup():


    if len(Query_All_Accounts()) == 0:
        return (jsonify({"Message":"There Are No Accounts"}))
    return (jsonify(Query_All_Accounts()))


@user_blueprint.route("/lookup/email", methods = ["POST"])
@adminRequired
def lookupEmail():


    data = request.get_json(force=True  )
    email = data["Email"]
    account = Query_Account_By_Email(email)
    if account:
        return ({'Account':{'Email': account.Email,'First_Name':account.First_Name,'Last_Name':account.Last_name ,'ID': account.id,"Position":account.Position}})
        
    else:
        return (jsonify({"Error":"There is no Account with that email"}))


@user_blueprint.route("/ban", methods = ["POST"])
@adminRequired
def Ban_Account():
    
    try:

        banned_by = Query_Account_By_ID(get_session_id())
        data = request.get_json(force=True)
        email = data["Email"]
        account = Query_Account_By_Email(email)
        ban_account(account.id,banned_by.Email)
        return (jsonify({"Message":"Account has been deactivated!"}))
        
    except Exception as e :

        print(e)
        return (jsonify({"Error":"There waes an error deactivating account!"})),500

   
@user_blueprint.route("/unban",methods=["POST"])
@adminRequired
def unban():


    try:

        unbanned_by = Query_Account_By_ID(get_session_id())
        data = request.get_json(force=True)
        email = data["Email"]
        account = Query_Account_By_Email(email)
        unban_account(account.id)
        log_unban(unbanned_by.Email,email)


        return ( jsonify("Account has been unbanned!"))


    except Exception as e:
        print(e)
        return(jsonify("There was an issue unbanning account"))



@user_blueprint.route("/roster")
@login_required
def Public_Roster():

    
    return (jsonify(Query_Roster()))



@user_blueprint.route("/inactive/get")
@adminRequired

def get_inactives():


    try:
        return (jsonify(Get_Inactives()))

    except:


        return (jsonify({"error":" There was an error querying accounts! Likely a database issues within the server"})),500






