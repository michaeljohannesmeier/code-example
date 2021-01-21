
import os
if os.path.isfile("example.db"):
    os.remove("example.db")
output_filename = os.path.join(os.path.dirname(__file__), "output.txt")
output_file = open(output_filename, "w")
#-#-#-#

#s  1: # Adding data
#an  : Adding data to the database
#sn 2: 
#a   : In this section we will have a look at how to add data to our users table which we created.
#sn 3: - Createing a session to interact with the database
#a   : Therefore, we first need to create a session object which is used to interact with the database
#sn 4: - Add a single object to the database  
#a   : Using this session object, we will see then, how to use it to add a single object to the database.
#sn 5: - Add multiple objects to the database 
#a   : Finally we will also see how to add multiple objects to the database.

#-#-#-#

#s  1: #Prerequisites
#a   : Prerequisites
#s  2:
#a   : Here are all the prerequisites you need in order to run the following examples. If you are not 
#      already familiar with this code, please go back to the previous sections. <break time="2000ms" />.
#c   : data-line: {3: "4-5", 4: "7-14", 5: "16"}
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
        return 'User(name="%s")' % (self.name)

Base.metadata.create_all(engine)
#s  3:
#a   : To recap quickly what we did so far. We generated an engine object and a base class.
#s  4:
#a   : Then we generated a user class. This class inherits from the base class. The database tablename 
#      is users and the colums are id of type integer, name of type string, fullname of type string and nickname also of type string.
#s  5:
#a   : Finally, we called the create all method passing our engine in order to actually create the users table.
#-#-#-#



#s  1: #Createing a session to interact with the database
#an  : Createing a session to interact with the database
#s  2: - A Session is needed for transactions with the database
#a   : To interact with the database, we first need to create a session. 
#      The session will then send all our transactions to the database
#      in a save way, so that no data get lost or corrupted. 
#      Also we can add multiple objects to our session and then send all our changes 
#      combined to the database.
#sn 3: - session maker <v-icon>arrow_right_alt</v-icon> session factory <v-icon>arrow_right_alt</v-icon> session
#a   : Sessions can be created out of a so called session factory. 
#      In order to create a session factory, we can use the session maker function.
#      So we will first use the session maker to create a session factory. 
#      And then we will use the session factory to create our actual session.
#sn 4: - Use sessionmaker function to create session factory
#a   : For that we first import the session maker function from sql-alchemy dot orm. 
#      Then we call the session maker function and pass the engine we created in the last section as an argument. 
#      This will create the session factory.
#sn 5: - Use SessionFactory to create session.
#a   : To finally create the session, we simply create an instance of the session factory.
#      This session object can now be used to interact with the database.
#c  : show-line: {4: 2}
from sqlalchemy.orm import sessionmaker
SessionFactory = sessionmaker(bind=engine)
session = SessionFactory()
#-#-#-#

#s  1: # Add a single object to the database  
#a   : Adding a single object to the database
#s  2: - Create an instance of user class
#a   : To add an entry to our database table, we can create an instance of our Users class
#      which we created earlier. In this example we create a instance with the name Ed, fullname Ed Jones 
#      and nickname Eddy.
#s  3: - Instance can be used as usually
#a   : The instance can be used as usually to print or change the users properties.
#      If we print user dot name, we will get the name of the user, in this case ed.
#sn 4:
#a   : Printing the nickname will return eddy. 
#s  5: 
#a   : So far we did not save the user to the database and we also did not specify the id property.
#      That is why the id property returns none.
#      The id property is handled automatically by sql alchemy after the object was saved to the database.
#s  6: - Add data to session: session.add(user)
#a   : To actually add data to the database, we first need to add the object to the session. 
#      Therefore we can use the sessions add method passing the user object as an argument. So far we only added the 
#      user to the session. The user is not yet saved into the database.
#s  7: - Call session.commit()
#a   : For that, we need to call commit on the session instance to commit our changes to the database.
#       With that, we have successfully added our first row to the database table.
#c   : show-line: {2: 1, 3: 3, 4: 5, 5: 7, 6: 9, 7: 10}
user = User(name='ed', fullname='Ed Jones', nickname='eddy')
user.name
output_file.write(str(user.name) + "\n")
user.nickname
output_file.write(str(user.nickname) + "\n")
user.id
output_file.write(str(user.id) + "\n")

session.add(user)
session.commit()

user.id
output_file.write(str(user.id) + "\n")
#s  8: Id is now set
#a   : If we call user dot id again, we see, that now the id field returns one. Sql alchemy automatically handled the id field 
#      and generated the id for us.

#-#-#-#

#s  1: # Add multiple objects to the database  
#a   : Add multiple objects to the database
#s  2: - User add_all to add to session
#a   : It is also possible to add multiple object to the database.
#      Therefore, the add_all method of the session object can be used.
#s  3: - Equivalent to session.add three times
#a   : This is simply a shorter way then instanciating each object and adding it one by one to the session.
#      So the lines one to five are equivalent to the lines 7 to 13, just that the lines 7-13 are more verbose.
#c   : show-line: {2: 5} data-line: {3: "1-5,7-13"}
session.add_all([
    User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    User(name='mary', fullname='Mary Contrary', nickname='mary'),
    User(name='fred', fullname='Fred Flintstone', nickname='freddy')])
session.commit()

user1 = User(name='wendy', fullname='Wendy Williams', nickname='windy')
user2 = User(name='mary', fullname='Mary Contrary', nickname='mary')
user3 = User(name='fred', fullname='Fred Flintstone', nickname='freddy')
session.add(user1)
session.add(user2)
session.add(user3)
session.commit()
#-#-#-#
