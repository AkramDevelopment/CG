from sqlalchemy import create_engine, Column, Integer, String, Numeric, DateTime, MetaData,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from backend.config.database import mysqlcred
import json
import datetime

config =  json.loads(mysqlcred) 

engine = create_engine(config["Mysql"]['uri'],
                       isolation_level="READ UNCOMMITTED")

connection = engine.connect()
Base = declarative_base()

class Account(Base):
    __tablename__="Account"

    id = Column("ID",Integer,primary_key=True)
    First_Name = Column('First_Name',String(32))
    Last_name = Column("Last_Name",String(32))
    Password = Column("Password",String(10000))
    Email = Column("Email",String(32))
    Group = Column("Group",String(32),default="Unconfirmed")
    Position = Column("Position",String(32),default="Member")
    Create_Date = Column("Create_Date", String(32),default = datetime.datetime.now())


    def __init__(self,First_Name,Last_Name,Email,Password):
        self.First_Name = First_Name
        self.Last_name = Last_Name
        self.Email = Email
        self.Password = Password


class Announcement(Base):
    __tablename__="Announcements"

    id = Column("ID",Integer,primary_key=True)
    title = Column('title',String(32))
    body = Column('body',String(32))
    Create_Date = Column("Create_Date", String(32),default = datetime.datetime.now())
    created_by = Column("Created_By", String(32))


    def __init__(self,title,body,created_by):
        self.title = title
        self.body = body
        self.created_by = created_by



class Banned_Accounts(Base):
    __tablename__="Banned_Accounts"

    id = Column("ID",Integer,primary_key=True)
    Account_ID = Column("Account_ID",Integer)
    Banned_By = Column("Banned_By",String(32))
    Ban_Date  = Column("Ban_Date",String(100),default = datetime.datetime.now())

    def __init__(self,Account_ID,Banned_By):
       self.Account_ID = Account_ID
       self.Banned_By = Banned_By



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


#Creates tables on the Mysql server, if they weren't already.
Base.metadata.create_all(engine)