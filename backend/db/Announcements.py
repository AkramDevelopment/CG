
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
class Announcement(Base):
    __tablename__="Announcements"

    id = Column("ID",Integer,primary_key=True)
    title = Column('title',String(32))
    body = Column('body',String(32))
    Create_Date = Column("Create_Date", String(32),default = datetime.datetime.now())


    def __init__(self,title,body):
        self.title = title
        self.body = body
        
def query_all_announcements():
    query = session.query(Announcement)
    result = []
    for row in query:
        result.append({"id":row.id,"title":row.title,'body':row.body,'create_date':row.Create_Date})

def query_announcement_by_id(id):
    query = session.query(Announcement).filter(Announcement.id == id)
    return (query)

def create_announcement(title,body):
    new_announcement = Announcement(title,body)
    session.add(new_announcement)
    session.commit()
    return('Announcement Created!')

def delete_announcement(id):
    try:
        announcement_query = session.query(Announcement).filter(Announcement.id == id).first()
        session.delete(announcement_query)
        session.commit()
        return ("Announcement Has Been Deleted!")
    except:
        return ("There Was An Error Deleting The Announcement, verify that there is an announcement with the unique ID provided.")


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






    
    






