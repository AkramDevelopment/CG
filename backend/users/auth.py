from functools import wraps
from flask import jsonify,request,session
from backend.db.Accounts import Query_Account_By_Email,Is_Admin,Is_Developer
from jwt import encode, decode

def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):  
       
        try:
            token = session['token']
            decode(token,'secret',algorithms='HS256')

        except:
            return jsonify({'error':"User Is Not Logged In!"}),401
        return f(*args,**kwargs)
    return decorated
        
    
def adminRequired(f):
    @wraps(f)
    def decorated(*args,**kwargs):  
        
        try:
            token = session['token']
            token=(decode(session['token'],'secret',algorithms='HS256'))
            if Is_Admin(token['id']) == False:
                return (jsonify({"error":"User Is Not Authorized To Access This Route"})),401
            #Will have a loggin system eventually to know who accessess what route at what time   
            print("Token Was Authorized into route")
                  
        except:
            return jsonify({"error":"User Is Not Logged In"}),401
        return f(*args,**kwargs)
    return decorated


def Developer_Required(f):
    @wraps(f)
    def decorated(*args,**kwargs):  
    
        try:
            token = session['token']
            token=(decode(session['token'],'secret',algorithms='HS256'))
            if Is_Developer(token['id']) == False:
                return (jsonify({"error":"User Is Not Authorized To Access This Route"})),401
            #Will have a loggin system eventually to know who accessess what route at what time   
            print("Token Was Authorized into route")
                  
        except:
            token=(decode(session['token'],'secret',algorithms='HS256'))
            print(token['id'])
            return jsonify({"error":"User Is Not Logged In"}),401
        return f(*args,**kwargs)
    return decorated