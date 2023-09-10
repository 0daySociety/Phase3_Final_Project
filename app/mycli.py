import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, School, Student, Teacher, Worker


DB_URL = 'sqlite:///Admin_School.db'

engine = create_engine(DB_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session=Session()
session.query(School).delete()



def testingDb(name:str, location:str):
    try:
        school=School(name=name, location=location)
        session.add(school)
        session.commit()
    except Exception as e:
        print("got this error",str(e))


testingDb("samuel","doe")










@click.group()
def cli():
    """
    School Database CLI
    """
    pass


@cli.command()
@click.argument("name")
@click.argument("location")
def create_school(name, location):
    
    try:
        session = Session()
        school = School(name=name, location=location)
        session.add(school)
        session.commit()
        session.close()
        print("|--------------Added School---------------|")
        print("|")
        click.echo(f"|        School '{name}' created at '{location}'. |")
        print("|-------------->>>>  Close >>>------------|")
    except Exception as e:
        print("got this error ",str(e))    
 

        

@cli.command()
@click.argument("table")
def get_all_Data(table):

    if table==Student:
        session=Session()
        students=session.query(Student)
        for student in students:
            print("me")
            click.echo(f"{student}")
    elif table==Worker:
        session=Session()
        workers=session.query(Worker)
        for worker in workers:

            click.echo(f"{worker}")   

    elif table==School:
        session=Session()
        schools=session.query(School)
        for school  in schools:

            click.echo(f"{school}")  
            
    elif table==Teacher:
        session=Session()
        teachers=session.query(Teacher)
        for teacher in teachers:

            click.echo(f"{teacher}")              
                     

        
           


@cli.command()
@click.argument("name")
@click.argument("grade")
def create_student(name, grade):
   
    session = Session()
    student = Student(name=name, grade=grade)
    session.add(student)
    session.commit()
    session.close()
    print("|-------------------------------|")
    print("|-------------------------")
    click.echo(f"| Student '{name}' with grade '{grade}' created.")
    print("|------------- >>> close <<<----------|")


@cli.command()
@click.argument("name")
@click.argument("subjects")
@click.argument("teaching_level")
def create_teacher(name, subjects, teaching_level):
  
    session = Session()
    teacher = Teacher(name=name, subjects=subjects, teaching_level=teaching_level)
    session.add(teacher)
    session.commit()
    print("|-------------------------------")
    print("|-------------------------")
    click.echo(f"|teacher name {name} subjects teaching {subjects} level of eduction {teaching_level} ")
    print("|------------- >>> close <<<----------")

if __name__ =="__main__":
    print("hello world ")
    cli()
