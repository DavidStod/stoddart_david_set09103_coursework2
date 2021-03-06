import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('sqlite:///tutorial.db', echo=True)

#create Session
Session = sessionmaker(bind=engine)
session = Session()

#create users
user = User("admin","password")
session.add(user)

user = User("python","python")
session.add(user)

user = User("jumpiness","python")
session.add(user)

user = User("Hunter97","Loarding1")
session.add(user)

# commit the record the database
session.commit()

session.commit()
