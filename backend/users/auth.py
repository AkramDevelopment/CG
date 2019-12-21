from functools import wraps
from flask import jsonify,request

from backend.db.Accounts import Query_Account_By_Email,Is_Admin
from jwt import encode, decode

def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):  
        token = request.args.get('token')
        if not token:
            return jsonify({"Error":"No Token Found"}),404
        try:
            data = decode(token,'secret',algorithms='HS256')
            
        except:
            return jsonify({"Error":"Token is Invalid!"})
        return f(*args,**kwargs)
    return decorated
        
    

def adminRequired(f):
    @wraps(f)
    def decorated(*args,**kwargs):  
        token = request.args.get('token')
        data = decode(token,'secret',algorithms='HS256')

        if Is_Admin(data['id']) == False:
            return ("Access Denied, User Is Not an Admin"),401
        if not token:
            return jsonify({"Error":"No Token Found"}),404
        try:
            decode(token,'secret',algorithms='HS256')
        except:
            return jsonify({"Error":"Token is Invalid!"})
        return f(*args,**kwargs)
    return decorated