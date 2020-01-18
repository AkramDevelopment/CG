
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
    Banned_By = ("Banned_By",String(32))
    ban_date = Column("Ban_Date",String(32),default = datetime.datetime.now())

    def __init__(self,Account_ID,Banned_By):
       self.Account_ID = Account_ID
       self.Banned_By = Banned_By



def ban_account(account_id,banned_by):
    session.add(account_id,banned_by)
    session.commit()


def unban_account(account_id):
    session.delete(account_id)
    session.commit()

def is_banned(id):
    query = session.query(Banned_Accounts).filter(Banned_Accounts.Account_ID == id)
    if query:
        return True
    else:
        return False



