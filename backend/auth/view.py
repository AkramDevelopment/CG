from functools import wraps

from flask import (Blueprint, Flask, jsonify, make_response, render_template,
                   request, session)
from jwt import decode, encode
from werkzeug.security import check_password_hash

from backend.config.fields import Account_Fields
from backend.db.Accounts import Query_Account_By_Email

auth_blueprint = Blueprint(
    'auth',
    __name__,
    template_folder='templates'
)




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
