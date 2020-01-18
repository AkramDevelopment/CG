from sqlalchemy import create_engine, Column, Integer, String, Numeric, DateTime, MetaData,Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from backend.db.config import mysqlcred
import datetime

engine = create_engine(mysqlcred['uri'],
                       isolation_level="READ UNCOMMITTED")
Session = sessionmaker(bind=engine)
session = Session()
connection = engine.connect()
Base = declarative_base()
class Event(Base):
    __tablename__="Events"
    id = Column("ID",Integer,primary_key=True)
    Event_Title = Column('Event_Title',String(32))
    Date_Start = Column("Date_Start",String(32))
    Date_End = Column("Date_End",String(32))
    Time_Start = Column("Time_Start",String(32))
    Time_End = Column("Time_End",String(32))
    Location = Column("Location", String(32))
    
    def __init__(self,Event_Title,Date_Start,Date_End,Time_Start,Time_End,Location):
        self.Event_Title = Event_Title
        self.Date_Start = Date_Start
        self.Date_End = Date_End
        self.Time_Start = Time_Start
        self.Time_End = Time_End
        self.Location = Location



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



