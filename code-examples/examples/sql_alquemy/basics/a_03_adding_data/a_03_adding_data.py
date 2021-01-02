
#-#-#-#

"""
# Addind data
## What you will learn  
- Createing a session to interact with the database  
- Add an object to the database  
- Add multiple objects to the database 
</br>
"""
#-#-#-#

"""
# Prerequisites
"""
# ``` python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine('sqlite:///example.db', echo=True)
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                            self.name, self.fullname, self.nickname)
Base.metadata.create_all(engine)
# ```

#-#-#-#

"""
<br>

## Createing a session to interact with the database 
To interact with the database, a session factory is created with the sql-alchemy sessionmaker class.  
This session factory class can then be used to create session objects. This session object 
will be used for all interactions with the databaase:
"""
# ``` python
from sqlalchemy.orm import sessionmaker
SessionFactory = sessionmaker(bind=engine)
session = SessionFactory()
# ```

"""
A connection will be established in the moment the session is used.  
The connection will be closed when the session is commited or closed.
<br>

## Add an object to the database  
To add an entry in our database table, instanciate an object of our Users class, then 
use the sessions add method to add the object to the session and finally commit the changes 
to the database with sesison.commit():
"""
# ``` python
user = User(name='ed', fullname='Ed Jones', nickname='eddy')
session.add(user)
session.commit()
# ```
"""
<br>

## Add multiple objects to the database  
It is also possible to add multiple object to the database on the same time. 
Therefore, the add_all method of the session object can be used:  
"""
# ``` python
session.add_all([
    User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    User(name='mary', fullname='Mary Contrary', nickname='mary'),
    User(name='fred', fullname='Fred Flintstone', nickname='freddy')])
session.commit()
# ```
