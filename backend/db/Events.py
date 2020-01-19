from sqlalchemy import create_engine, Column, Integer, String, Numeric, DateTime, MetaData,Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from backend.config.database import mysqlcred
from backend.db.database import Event
import datetime
import json

config =  json.loads(mysqlcred) 

engine = create_engine(config["Mysql"]['uri'],
                       isolation_level="READ UNCOMMITTED")
Session = sessionmaker(bind=engine)
session = Session()
connection = engine.connect()



def create_event(Event_Title,Date_Start,Date_End,Time_Start,Time_End,Location):


    new_event = Event(Event_Title,Date_Start,Date_End,Time_Start,Time_End,Location)
    session.add(new_event)
    session.commit()
    return ("New Event Added Successfully!")



def remove_event(id):


    query = session.query(Event).filter(Event.id == id).first()
    session.delete(query)
    session.commit()
    return ("Event Has Been Successfully Removed!")


def query_events():


    query = session.query(Event)
    result = []
    for row in query:
        result.append({"id":row.id,"event_title":row.Event_Title,'date_start':row.Date_Start,"date_end":row.Date_End,'time_start':row.Time_Start,
        "time_end":row.Time_End,'location':row.Location})
    return (result)


def query_by_id(id):


    query = session.query(Event).filter(Event.id == id).first()
    return (query)
