from sqlalchemy import create_engine, Column, Integer, String, Numeric, DateTime, MetaData,Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from backend.db.database import Meeting_Notes
from backend.config.database import mysqlcred
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




def query_all():
    query = session.query(Meeting_Notes)
    result = []
    
    for note in query: 
        result.append({"title":note.Title,"body":note.Body,"created_by":note.Created_By,"created_date": note.Created_Date})
    return (result)


def query_by_id(id):
    query = session.query(Meeting_Notes).filter(Meeting_Notes.id == id).first()

    return({"title":query.Title,"body":query.Body,"created_by":query.Created_By,"created_date":query.Created_Date})




