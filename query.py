import datetime
from sqlalchemy import create_engine,func
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Puppy, Shelter
engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

first=session.query(Puppy).order_by(Puppy.name).all()
for x in first:
    print(x.name)
session.close()
today=datetime.date.today()
sixmonthindays=6*30
date_before_six_month=today-datetime.timedelta(days=sixmonthindays)

second=session.query(Puppy).filter(Puppy.dateOfBirth >= date_before_six_month).all()
for x in second:
    print(x.dateOfBirth)

third=session.query(Puppy).order_by(Puppy.weight).all()
for x in third:
    print(x.weight)

fourth=session.query(Shelter.name,func.count(Shelter.id).label("totalcount"),Puppy).filter(Shelter.id==Puppy.shelter_id).group_by(Shelter.id).all()
for x in fourth:
    print(x.name + " " +str(x.totalcount))