from sqlalchemy import create_engine, Column, Integer, String, Numeric, DateTime, MetaData,Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

engine = create_engine('mysql://root:!Amohammed21@localhost/CG',
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
    Positon = Column("Position",String(32),default="Member")
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



def Add_Admin(id):
    query = session.query(Account).filter(Account.id == id).first()
    query.Positon = "Admin"
    session.commit()
    return("Admin Privlages have been added!")

def remove_User(id):
    result = session.query(Account).filter(Account.id == id).first()
    session.delete(result)
    session.commit()


def Is_Admin(id):
    user = session.query(Account).filter(Account.id == id).first()
    if user.Positon == "Admin":
        return True
    else:
        return False

        
def Query_Account_By_Username(Email):
    query = session.query(Account).filter(Account.Email == Email).first()
    return (query)





