from sqlalchemy import create_engine, Column, Integer, String, Numeric, DateTime, MetaData,Boolean
from backend.db.Groups import query_groups,query_group_by_id
from backend.db.Accounts import Query_All_Accounts
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
        return ("error")
    else:
        pass






print(add_member("1",'1','asd'))
