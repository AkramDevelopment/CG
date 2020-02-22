
from sqlalchemy import create_engine, Column, Integer, String, Numeric, DateTime, MetaData,Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from backend.config.database import mysqlcred
from backend.db.database import Announcement
import datetime
import json


config =  json.loads(mysqlcred) 
engine = create_engine(config["Mysql"]['uri'],
                       isolation_level="READ UNCOMMITTED")
Session = sessionmaker(bind=engine)
session = Session()
connection = engine.connect()
Base = declarative_base()

        
def query_all_announcements():
    query = session.query(Announcement)
    result = []
    for row in query:
        result.append({"id":row.id,"title":row.title,'body':row.body,'create_date':row.Create_Date})
    return(result)

def query_announcement_by_id(id):
    query = session.query(Announcement).filter(Announcement.id == id).first()
    announcement = {"id": query.id,"title":query.title,"body":query.body,"created_by":query.created_by,"created_Date":query.Create_Date}
    return (announcement)

def create_announcement(title,body,created_by):
    new_announcement = Announcement(title,body,created_by)
    session.add(new_announcement)
    session.commit()
    return('Announcement Created!')

def delete_announcement(id):

    announcement_query = session.query(Announcement).filter(Announcement.id == id).first()
    session.delete(announcement_query)
    session.commit()
    return ("Announcement Has Been Deleted!")
    


def edit_announcement(id,title,body):
    try:
        announcement_query = session.query(Announcement).filter(Announcement.id == id).first()
        announcement_query.id = id
        announcement_query.title = title
        announcement_query.body = body
        session.commit()
        return ("Announcement updated successuly!")
    except:
        return ("There was an error editing the announcement")




create_announcement("Test","Remember to instlal kali Linux on a virtual machine by sunday for the next cyber gladiator meeting","")


