from sqlalchemy import create_engine, Column, Integer, String, Numeric, DateTime, MetaData,Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from backend.config.database import mysqlcred
from backend.db.database import Account,Roster
from backend.db.Groups import query_group_by_id
import datetime
import json
import datetime

config =  json.loads(mysqlcred) 
engine = create_engine(config["Mysql"]['uri'],
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
    query.Security_Clerance = "Admin"
    session.commit()
    return("Admin Privilege have been added!")


def Activate_User(secondary_email,id):


    account = Query_Account_By_ID(id)
    if account:

        account.Secondary_Email = secondary_email
        account.Security_Clerance = "member"
        session.commit()
    else:

        return False

def Is_Admin(id):


    user = session.query(Account).filter(Account.id == id).first()
    if user.Security_Clerance == "Admin":
        return True
    else:
        return False

def Is_Developer(id):


    user = session.query(Account).filter(Account.id == id).first()
    if user.Security_Clerance == "Developer":
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
    if query:

        return (query)
    else:
        return False
    

def Query_All_Accounts():


    query = session.query(Account)
    result = []
    for account in query:
        result.append({"ID":account.id,'First_Name': account.First_Name, "Last_Name": account.Last_name, "Email": account.Email,"Security_Clerance": account.Security_Clerance})
    return (result)



def Query_Roster():

    
    query = session.query(Account)
    result = []
    for account in query:
        result.append({"First_Name":account.First_Name,'Last_Name':account.Last_name,'Date_Joined':account.Create_Date})
    return(result)


def Get_Inactives():

    query = session.query(Account).filter(Account.Security_Clerance == "unregistered")
    result = []
    for account in query:
        result.append({"ID":account.id,'First_Name': account.First_Name, "Last_Name": account.Last_name, "Email": account.Email,"Security_Clerance": account.Security_Clerance})
    return ({result})





def get_groups(account_id):
    query = session.query(Roster).filter(Roster.Account_ID == account_id)
    if query:

        result = []
        for group in query:
            group_name = query_group_by_id(group.Group_ID)
            result.append({'group_name': group_name.Group_Name, 'is_admin': group.Is_Admin})
        return (result)
    else:
        return False



