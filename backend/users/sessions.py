from backend.db.Accounts import Query_Account_By_ID
from flask import session
from jwt import decode


def get_session_id():
    token = decode(session['token'],'secret',algorithms='HS256')
    return (token['id'])


