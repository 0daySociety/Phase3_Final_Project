
from datetime import datetime
from sqlalchemy import (Column,Integer, String,ForeignKey,
                        DateTime,PrimaryKeyConstraint)
from sqlalchemy.orm import declarative_base

Base =declarative_base()
# this file contains all the schema for my school database 
#only the relevant data is available here 
# this file will contain School class ,Student class , workers class and techers class 
# they will be linked via one to one and one to many relationship


class School(Base):
    # creating the columns for the school table 
    __tablename__="school"

    __tableargs__=PrimaryKeyConstraint(name='id')
    id=Column(Integer(),primary_key=True)
    name=Column(String(),nullable=False)
    location=Column(String(),nullable=False)


class Student(Base):
    __tablename__='students'
    id=Column(Integer(),primary_key=True)
    name=Column(Integer(),nullable=False)
    grade=Column(String(),nullable=False)
    time_in=Column(DateTime(),default=datetime.now())
   
class Teacher(Base):
    __tablename__='teachers'
    id=Column(Integer(),primary_key=True)
    name=Column(Integer(),nullable=False)
    subjects=Column(String(),nullable=False) #a techer can teach more that one subject 
    teaching_level=Column(String(),nullable=False)
    time_in=Column(DateTime(),default=datetime.now())

    
class Worker(Base):
    __tablename__="workers"
    id =Column(Integer(),primary_key=True)
    name=Column(Integer(),nullable=False)
    time_in=Column(DateTime(),default=datetime.now)

