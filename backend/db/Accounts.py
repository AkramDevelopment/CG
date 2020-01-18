from sqlalchemy import create_engine, Column, Integer, String, Numeric, DateTime, MetaData,Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from backend.db.config import mysqlcred
import datetime

engine = create_engine(mysqlcred['uri'],
                       isolation_level="READ UNCOMMITTED")
Session = sessionmaker(bind=engine)
session = Session()
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
    Is_Banned = Column("Is_Banned",Boolean,default = False)
    Banned_By = Column("Banned_By",String(32) )
    Create_Date = Column("Create_Date", String(32),default = datetime.datetime.now())


    def __init__(self,First_Name,Last_Name,Email,Password):
        self.First_Name = First_Name
        self.Last_name = Last_Name
        self.Email = Email
        self.Password = Password


def Add_User(first_name,last_name,email,password):
    hashed = generate_password_hash(password, method="sha256")
    password = hashed
    newUser = Account(first_name,last_name,email,hashed)
    session.add(newUser)
    session.commit()
    return ("User Has been Successfully Created!")

   

def Deactivate_Account(id,banned_by):
    query = session.query(Account).filter(Account.id == id ).first()
    query.Is_Banned = True
    query.Banned_By = banned_by
    session.commit()
    return ("Account Has Been Deactivated")

def Add_Admin(id):
    query = session.query(Account).filter(Account.id == id).first()
    query.Position = "Admin"
    session.commit()
    return("Admin Privilege have been added!")

def remove_User(id):
    result = session.query(Account).filter(Account.id == id).first()
    session.delete(result)
    session.commit()
    return ("User Has Been Removed Successfully!")


def Is_Admin(id):
    user = session.query(Account).filter(Account.id == id).first()
    if user.Position == "Admin":
        return True
    else:
        return False

def Is_Developer(id):
    user = session.query(Account).filter(Account.id == id).first()
    if user.Position == "Developer":
        return True
    else:
        return False       
        
def Query_Account_By_Email(Email):
    query = session.query(Account).filter(Account.Email == Email).first()
    if query:
        print(query)
        return (query)
    else:
        return ("There Is No Account With That Email")
def Query_Account_By_ID(id):
    query = session.query(Account).filter(Account.id == id).first()
    return (query)
    

def Query_All_Accounts():
    query = session.query(Account)
    result = []
    for account in query:
        result.append({"ID":account.id,'First_Name': account.First_Name, "Last_Name": account.Last_name, "Email": account.Email,"Position": account.Position})
    return (result)

def Query_Roster():
    query = session.query(Account)
    result = []
    for account in query:
        result.append({"First_Name":account.First_Name,'Last_Name':account.Last_name,'Date_Joined':account.Create_Date})
    return(result)


