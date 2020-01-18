
from sqlalchemy import create_engine, Column, Integer, String, Numeric, DateTime, MetaData,Boolean
from backend.db.config import mysqlcred
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime

engine = create_engine(mysqlcred['uri'],
                       isolation_level="READ UNCOMMITTED")
Session = sessionmaker(bind=engine)
session = Session()
connection = engine.connect()
Base = declarative_base()


class Banned_Accounts(Base):
    __tablename__="Account"

    id = Column("ID",Integer,primary_key=True)
    Account_ID = ("Account_ID",Integer)
    ban_date = Column("Ban_Date",String(32),default = datetime.datetime.now())

    def __init__(self,Account_ID):
       self.Account_ID = Account_ID

