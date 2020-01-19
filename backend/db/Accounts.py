from sqlalchemy import create_engine, Column, Integer, String, Numeric, DateTime, MetaData,Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from backend.db.config import mysqlcred
from backend.db.database import Account
import datetime

engine = create_engine(mysqlcred['uri'],
                       isolation_level="READ UNCOMMITTED")
Session = sessionmaker(bind=engine)
session = Session()
connection = engine.connect()
Base = declarative_base()


def Add_User(first_name,last_name,email,password):


    hashed = generate_password_hash(password, method="sha256")
    password = hashed
    newUser = Account(first_name,last_name,email,hashed)
    session.add(newUser)
    session.commit()
    return ("User Has been Successfully Created!")

   

def Add_Admin(id):


    query = session.query(Account).filter(Account.id == id).first()
    query.Position = "Admin"
    session.commit()
    return("Admin Privilege have been added!")


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



