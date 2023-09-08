from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base,School

# this file is were we are handling the transations and sessions of the database 

if __name__ =="__main__":
    # tracking my errors in the database sessions using try statements
    try:
        
        engine =create_engine('sqlite:///Admin_School.db')  #where the db is stored 
        Base.metadata.create_all(engine) #linking all tables that inherite the Base class to the Admin db location
        Session=sessionmaker(bind=engine) # creating session to link to the database 
        session=Session()

        # below will contain all the session query for communicating with the database 


    except Exception as e:
        print("Sorry encounted this error", str(e))

