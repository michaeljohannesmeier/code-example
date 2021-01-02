import os
output_filename = os.path.join(os.path.dirname(__file__), "output.txt")
output_file = open(output_filename, "w")

# prerequisites
from sqlalchemy import create_engine
engine = create_engine('sqlite:///example.db', echo=True)

#-#-#-#

#s 1: #Basic mapping
#audi: In this part we will talk about the basic mapping
#s 2: What you will learn
#audi: Here is what you will learn:
#s 3: - Createing a python class
#audi: You will learn how to create a python class which inherits from the sql alchemy base class.
#s 4: - Using this class to create the database table
#audi: How to use this class to create or map it to a database table.
#s 5: - Create an instance of the python class
#audi: And how to create an instance of the python class. This instance is then later used to save an object to the database.

#-#-#-#

#s 1: #Defining a python class and map it to a database table
#audi: Defining a python class and map it to a database table
#s 2: 
#audi: To define a database table, it is possible to define a python class which class-propertys will then be mapped to database tables.
#s 3: - Sql alchemy imports
#audi: For that we will first make some imports from sql alchemy which we will need. We import the Column class and the Integer and String class. And we also import the declarative base function.
#s 4: - Define sql alchemy base class
#audi: Then we will use the declarative base function which we imported to create an instance of the base class.
#s 5: - Define python class
#audi: Then we define a python class called User. The python class needs to inherit from the sql-alchemy Base class. 
#s 6: - Add table properties
#audi: The class needs to have the table name property. It must be exactly _ _ tablename _ _. This property defines the sql table name. In this case the table name will be users.
#s 7: - Add columns
#audi: Then we can add the colums which we want to have in our database table. Each class-property we add will be mapped to a database column if the property is an instance of the sql alchemy column class. In our case we added the propertys ID, name, fullname and nickname.
#s 8: - Add type of database column to column class
#audi: When we define the column, we can add the type of the database to the column instanciation. In our example, the ID column is of type Integer and the other 3 columns are of type string.
#s 9: 
#audi: To uniquely identify each row in our datatable, we add primary key equals true to the ID column.
#s 10: - String representation
#audi: We also add a string representation of an output. This representation defines how a row will look like for us in python code when we print it.
#s 11: 
#audi: So, to sum up, here we defined a python class called User. Because this class inherits from the sql-alchemy base class, sql-alchemy can use it to create the table with all the columns we defined. We will see now how that works.
#c: show-line: {3: 2, 4:4, 5: 5, 6:6, 7: 11, 8:11, 9: 11} data-line: {8: "8-11", 9: "8", 10: "13-15"}
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
        return 'User(name="%s", fullname="%s", nickname="%s")' % (
                self.name, self.fullname, self.nickname)
#-#-#-#

#s 1: #Creating the database table
#audi: Creating a database table
#s 2: Create database table with the following code:
#audi: After we have defined our first mapper class, we can create the database table with the following code:
#c: show-line: {2: 1}
Base.metadata.create_all(engine)
#s 3:
#audi: So the method create_all will create all defined tables, in our case the user table will be created. The method takes the engine we define earlier as an input argument so that a connection to the database can be established.

#-#-#-#

#s 1: #Creating an instance of the Users class
#audi: Creating an instance of the Users class
#s 2: Create instance of class with:
#audi: The python User class can be used as usually to create instances out of it. Here, we create a User with name ed, fullname Ed Jones and nickname eddy.
#s 3: 
#audi: If we print ed _ user dot name, we will get the name of the user, in this case ed.
#s 4:
#audi: Printing the nickname will return eddy.
#c: show-line: {2: 1, 3:3, 4:5, 5: 7}
ed_user = User(name='ed', fullname='Ed Jones', nickname='eddy')
ed_user.name
output_file.write(str(ed_user.name) + "\n")
ed_user.nickname
output_file.write(str(ed_user.nickname) + "\n")
ed_user.id
output_file.write(str(ed_user.id) + "\n")
#s 5: User so far not saved to the database, so id = None
#audi: Because we use the ID property as our primary key, this field is handled automatically by sql. So far we did not save the user to the database. That is why the ID property returns none. Saving an object to the database is shown in the next chapter.

#-#-#-#
output_file.close()
