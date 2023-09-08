from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random
from models import Base,School,Teacher,Student,Worker
fake=Faker()

# this file is were we are handling the transations and sessions of the database 

if __name__ =="__main__":
    # tracking my errors in the database sessions using try statements
    try:
        
        engine =create_engine('sqlite:///Admin_School.db')  #where the db is stored 
        Base.metadata.create_all(engine) #linking all tables that inherite the Base class to the Admin db location
        Session=sessionmaker(bind=engine) # creating session to link to the database 
        session=Session()

        # below will contain all the session query for communicating with the database 
    #    to avoid the table to fill on each commit , i first delete all the data present , then add the new data 
        session.query(School).delete()
        session.query(Student).delete()
        session.query(Teacher).delete()
        session.query(Worker).delete()
         # using a list datatype  for the school table 



        #  populating the school table 
        schools=[School(
            name=fake.name(),
            location=fake.city()
            )
            for school in range(10)
            ]
        
        session.bulk_save_objects(schools)
        session.commit()


        # populating the school database 
        fake_grade =( "Kindergarten",
                     "1st Grade",
                     "2nd Grade",
                     "3rd Grade",
                    "4th Grade",
                    "5th Grade",
                    "6th Grade",
                    "7th Grade",
                    "8th Grade",
                    "9th Grade",
                    "10th Grade",
                    "11th Grade",
                    "12th Grade")
        
        student=[
            Student(
                name=fake.name(),
                grade=fake_grade[random.randint(1,len(fake_grade)-1)]
            )
            for student in range(10)
        ]
        session.bulk_save_objects(student)
        session.commit()
        

        #populating the teachers table  


        fake_subject =( 
    "Mathematics",
    "Science",
    "History",
    "English",
    "Physics",
    "Chemistry",
    "Biology",
    "Computer Science",
    "Geography",
    "Economics",
    "Psychology",
    "Sociology",
    "Literature",
    "Art",
    "Music",
    "Physical Education",
    "Spanish",
    "French",
    "German",
    "Latin")
        fake_education_level =('High School', 'Associate Degree', 'Bachelor\'s Degree', 'Master\'s Degree', 'Doctorate')

        # using a list datatype  for the school table
        teachers=[
            Teacher(
                name=fake.name(),
                subjects=fake_subject[random.randint(1,len(fake_subject)-1)],
                # generating a random education level 
                teaching_level=fake_education_level[random.randint(1,len(fake_education_level)-1)]
                )
                for teacher in range(10)
        ]
        session.bulk_save_objects(teachers)
        session.commit()

        # populating the workers table  

        workers=[
            Worker(name=fake.name())
             for worker in range(10)
        ]
        session.bulk_save_objects(workers)
        session.commit() 
        


    except Exception as e:
        print("Sorry encounted this error", str(e))

