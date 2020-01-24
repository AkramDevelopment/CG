from sqlalchemy import create_engine, Column, Integer, String, Numeric, DateTime, MetaData,Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Blueprint,Flask,render_template,session,request,jsonify,make_response,session
from backend.config.database import mysqlcred
from backend.db.database import Groups
import json


config =  json.loads(mysqlcred) 
engine = create_engine(config["Mysql"]['uri'],
                       isolation_level="READ UNCOMMITTED")
Session = sessionmaker(bind=engine)
session = Session()
connection = engine.connect()


def create_group(group_name, group_description):
    
    Group = Groups(group_name,group_description)
    session.add(Group)
    session.commit()
    return ("Group Created!")


def delete_group(id):
    query = session.query(Groups).filter(Groups.ID == id).first()
    session.delete(query)
    session.commit()
    return ("Group deleted!")


def edit_group(id,group_name,group_description):

    Group = session.query(Groups).filter(Groups.ID == id).first()
    Group.Group_Name = group_name
    Group.Group_Description = group_description
    return ("Edit complete!")
    

def query_groups():

    query = session.query(Groups)
    result = []
    for group in query:
        result.append({"id":group.ID,"group-name": group.Group_Name,"group-desciption" : group.Group_Description})

    return(result)


