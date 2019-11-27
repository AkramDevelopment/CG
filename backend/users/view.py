from flask import Blueprint,Flask,render_template,session,request
from werkzeug.security import check_password_hash
from backend.db.db import Query_Account_By_Email,Add_User
user_blueprint = Blueprint(
    'user',
    __name__,
    template_folder='templates'
)

@user_blueprint.route('/register', methods = ["POST"])
def createAccount():
    new_user =  {"First_Name":request.form["first_name"],"Last_Name":request.form["Last_Name"],"Email":request.form["Email"],"Password":request.form["Password"]}
    if Query_Account_By_Email(new_user["Email"]):
        return ("There Is Already An Account Associated With that Email!")
    Add_User(new_user["First_Name"],new_user["Last_Name"],new_user["Email"],new_user["Password"])

    

@user_blueprint.route('/register', methods = ["GET"])
def createAccountGET():
    return render_template('createAccount.html')

           
       
  



@user_blueprint.route("/auth/login", methods = ["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    account = Query_Account_By_Email(username)
    if not check_password_hash(account.password,password):
        return ("Invalid Credentials")
    else:
        return ("You may pass")



    

