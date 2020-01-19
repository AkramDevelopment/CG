
from sqlalchemy import create_engine, Column, Integer, String, Numeric, DateTime, MetaData,Boolean
from backend.db.database import Banned_Accounts
from backend.config.database import mysqlcred
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime
import json


config =  json.loads(mysqlcred) 
engine = create_engine(config["Mysql"]['uri'],
                       isolation_level="READ UNCOMMITTED")
Session = sessionmaker(bind=engine)
session = Session()
connection = engine.connect()



def ban_account(account_id,banned_by):


    banned_account = Banned_Accounts(account_id,banned_by)
    session.add(banned_account)
    session.commit()
    return ("Account Banned")


def unban_account(account_id):


    query = session.query(Banned_Accounts).filter(Banned_Accounts.Account_ID == account_id).first()
    session.delete(query)
    session.commit()
    return ("Account Unbanned")
    

def is_banned(id):


    query = session.query(Banned_Accounts).filter(Banned_Accounts.Account_ID == id)
    if query:


        return True
    else:


        return False


