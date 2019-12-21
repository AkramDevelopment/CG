
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
        

def create_announcement(title,body):
    new_announcement = Announcement(title,body)
    session.add(new_announcement)
    session.commit()
    return('Announcement Created!')
