import os
output_filename = os.path.join(os.path.dirname(__file__), "output.txt")
output_file = open(output_filename, "w")

#     prerequisites
from sqlalchemy import create_engine
engine = create_engine('sqlite:///example.db', echo=True)

#-#-#-#

#s  1: #Basic mapping
#an  : In this part we will talk about the basic mapping
#s  2: What you will learn
#an  : Here is what you will learn:
#sn 3: - Creating a python class
#a   : You will learn how to create a python class which inherits from the sql alchemy base class.
#sn 5: - Creating a database table
#a   : And how to use this class to create our first database table.
#      This instance is then later used to save an object to the database.

#-#-#-#

#s  1: #Defining a python class and map it to a database table
#an  : Defining a python class and map it to a database table
#sn 2: 
#a   : To define a database table, it is possible to define a python class which class-propertys will 
#     then be mapped to database tables.
#     For that we will first make some imports from sql alchemy which we will need. 
#     We import the Column class and the Integer and String class (see line 1). 
#     And we also import the declarative base function (line 2).
#sn 3: - Define sql alchemy base class
#a   : Then we will use the declarative base function which we imported to create an instance of the 
#     base class.
#sn 4: - Define User class
#a   : Then we define a python class called User. The python class needs to inherit from the 
#     sql-alchemy Base class. 
#sn 5: - Add __tablename__ property
#a   : The class needs to have the table name property. It must be exactly _ _ tablename _ _. 
#     This property defines the sql table name. In this case the table name will be users.
#sn 6: - Add columns
#a   : Then we can add the colums which we want to have in our database table. 
#     Each class-property we add will be mapped to a database column if the property is an instance of the sql alchemy column class. In our case we added the propertys id, name, fullname and nickname.
#sn 7: - Add type of database column to Column class
#a   : When we define the column, we can add the type of the database to the column instanciation. 
#     In our example, the id column is of type Integer and the other 3 columns are of type string.
#sn 8: 
#a   : To uniquely identify each row in our datatable, we add primary key equals true to the id column.
#sn 9: - String representation
#a   : We also add a string representation of an output. This representation defines how a row will look 
#     like for us in python code when we print it.
#sn 10: 
#a   : So, to sum up, here we defined a python class called User. 
#     Because this class inherits from the sql-alchemy base class, sql-alchemy can use it to create the 
#     table with all the columns we defined. We will see now how that works.
#c   : show-line: {2: 2, 3:4, 4: 5, 5:6, 6: 11, 7:11, 8: 11} 
#      data-line: {7: "8-11", 8: "8", 9: "13-15"}
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return 'User(name="%s")' % (self.name)

#-#-#-#

#s  1: #Creating a database table
#an  : Creating a database table
#sn 2: Create database table with the create_all method passing the engine object
#a   : After we have defined our first mapper class, we can create the database table with the following code:
#c   : show-line: {2: 1}
Base.metadata.create_all(engine)
#sn 3:
#a   : So the method create_all will create all defined tables, in our case the user table will be created. 
#     The method takes the engine we define earlier as an input argument so that a connection to the database 
#     can be established.
#     Because the User class inherited from the Base class, the Base class can now be used to generate our 
#     table and the table columns.
#     The execution of create_all will generate a file called example dot db which will have our table users 
#     defined.
#     <break time="2000ms"/> In the next chapter we will see how to add data to this table.



#-#-#-#
#s  1: #Creating an instance of the Users class
#an  : Creating an instance of the Users class
#sn 2: Create instance of class with:
#a   : The python User class can be used as usually to create instances out of it. 
#     Here, we create a User with name ed, fullname Ed Jones and nickname eddy.
#sn 3: 
#a   : If we print ed _ user dot name, we will get the name of the user, in this case ed.
#sn 4:
#a   : Printing the nickname will return eddy.
#c   : show-line: {2: 1, 3:3, 4:5, 5: 7}
ed_user = User(name='ed', fullname='Ed Jones', nickname='eddy')
ed_user.name
output_file.write(str(ed_user.name) + "\n")
ed_user.nickname
output_file.write(str(ed_user.nickname) + "\n")
ed_user.id
output_file.write(str(ed_user.id) + "\n")
#sn 5: User so far not saved to the database, so id = None
#a   : So far we did not save the user to the database and we also did not specify the id property.
#     That is why the id property returns none.
#     The id property is handled automatically by sql alchemy after the object was saved to the database.
#     Saving an object to the database is shown in the next chapter.
output_file.close()
