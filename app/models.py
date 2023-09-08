
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
    pass 
class Teacher(Base):
    pass
class Student(Base):
    pass
class Worker(Base):
    pass 

