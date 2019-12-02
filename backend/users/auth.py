from functools import wraps
from flask import jsonify,request

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
        if not token:
            return jsonify({"Error":"No Token Found"}),404
        try:
            data = decode(token,'secret',algorithms='HS256')
            return (data)
        except:
            return jsonify({"Error":"Token is Invalid!"})
        return f(*args,**kwargs)
    return decorated