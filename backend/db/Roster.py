from sqlalchemy import create_engine, Column, Integer, String, Numeric, DateTime, MetaData,Boolean
from backend.db.Groups import query_groups,query_group_by_id
from backend.db.Accounts import Query_All_Accounts
from backend.db.database import Roster
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from backend.config.database import mysqlcred
import datetime
import json

config =  json.loads(mysqlcred) 

engine = create_engine(config["Mysql"]['uri'],
                       isolation_level="READ UNCOMMITTED")
Session = sessionmaker(bind=engine)
session = Session()
connection = engine.connect()



def add_member(account_id, group_id,is_admin):

    query = query_group_by_id(group_id)

    if query == False:


        return ("There is no group by that ID!")
    else:

        
        new_member = Roster(account_id,group_id,is_admin)
        session.add(new_member)
        session.commit()
        return ("Member added to roster!")



def remove_member(account_id,group_id):


    group_query = query_group_by_id(group_id)

    if group_query == False:
        return ("There is no group by that ID!")

    query = session.query(Roster).filter(Roster.group_ID== group_id).filter(Roster.account_ID == account_id)
    session.delete(query)
    session.commit()
    return ("Member removed from group successfully!")
    




def add_admin(account_id,group_id):

    
    query = session.query(Roster).filter(Roster.Account_ID == account_id).filter(Roster.Group_ID == group_id).first()
    if query:

        query.Is_Admin == True
        session.commit()
        return ("Account has been updated to admin!")
    else:
        return False




def remove_admin(account_id,group_id):


    query = session.query(Roster).filter(Roster.Account_ID == account_id).filter(Roster.Group_ID == group_id).first()
    if query:


        query.Is_Admin == False
        session.commit()
        return ("Admin rights revoked for account!")
    else:
        return False


        