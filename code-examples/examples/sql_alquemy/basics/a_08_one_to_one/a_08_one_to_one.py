import os
if os.path.isfile("example.db"):
    os.remove("example.db")
output_filename = os.path.join(os.path.dirname(__file__), "output.txt")
output_file = open(output_filename, "w")
#-#-#-#

#s  1: One to one relationship
#a   : One to one relationship
#so 2: <div :style="{position: 'absolute', top: 0, right: 0, background: 'white', color: 'red'}"> Hint: this is a hint</div> 
#a   : In this chapter, we will have a closer look at the one to one relationship.
#s  3: <div>Unidirectional:</div>
#      <div class="ml-3">- Defining users table and addresses table</div>
#a   : We will first have a look at the unidirectional case. 
#      Therefore, we will define two tables. A users table and an addresses table.
#      We will see how to build a one to one relationship between this two tables.
#s  4: <div class="ml-3">- Creating tables and adding data</div>
#a   : Then, we will create the actual tables which we defined, and populate the tables with data to see
#      how the data is related to each other for the unidirectional case.
#s  5: <div>Bidirectional:</div>
#      <div class="ml-3">- Defining users table and addresses table</div>
#a   : Then we will have a look at the bidirectional case.
#      We will define the same two tables, users and addresses.
#s  6: <div class="ml-3">- Creating tables and adding data</div>
#a   : Then, we will also create the tables and populate it with data, to see how the
#      data is related in the bidirectional case.


#-#-#-#
#s  1: Defining users table and addresses table (unidirectional)
#a   : Defining users table and addresses table , unidirectional
#s  2: One to one: One user has one address
#a   : To demonstrate the one to one relationship, we will again look at the example of users with addresses.
#      Each user should only have one address related to him. In this first example we will show how to 
#      create a unidirectional relationship. Unidirectional relationship means, that in our python code,
#      we can only reference from a user to its address, but not the other way around. So, we can not
#      reference from an address to its user. We will see what that means in a second.
#s  3:
#a   : To generate our two mapper classes, we first make all the imports we need.
#      The new imports, are the imports in line 5 and 6. 
#      To define a relationship, we need the foreign key class
#      imported from sql alchemy, as well es the relationship function imported from sql alchemy dot ORM.
#s  4:
#a   : Next, we define our engine object, as well as the base class, like in the examples before.
#s  5: 
#a   : Then, we define the user class, which will define the users table. 
#      This time, the users table will only have two columns, the ID 
#      column of type integer, and the name column of type string.
#s  6: 
#a   : Additionally to the columns, we now define our first relationship. 
#      Therefore, we define a property called address
#      and we use the relationship function to define the property. 
#      The relationship function takes
#      the class name of the python class which it references, as a first argument. 
#      In our case the class name, address, is passed as
#      a first argument. Further, we define the second argument, use list. 
#      This argument determines, if the property should be
#      defined as a list or as a single object. In our case we only allow one address for every user. That is 
#      why we set use list, to false. <break time="2000ms"/> Note, that the address property
#      is only a property on our python user class. There will be no column called address in the users table.
#      This property only exists in our python code in order to access the users address.
#s  7: 
#a   : Next, we define the addresses table by defining the address class. 
#      The addresses table should have the columns ID, of type integer, and city
#      of type string.
#s  8:
#a   : We also define a third column called user _ ID. 
#      This column will be of type integer and it uses the foreign key class
#      which we imported, as an second argument. 
#      The foreing key class takes the column we want to reference as an argument. 
#      In our case, we reference the column ID of the table users, with users dot ID.
#      This column holds the information, to which user an address belongs. So in this
#      column, we will save the id of the user, which will be referenced with this address.
#s  9:
#a   : It is important to note, that the column ID, of the users table, 
#      and the column user _ ID, both must have the same type,
#      in our case the type integer. Using the foreign key class assures, 
#      that only values which are present in the
#      ID column of the users class can be saved in the user _ ID column. 
#      This is called a database constraint. Saving a user with an ID which does not 
#      exist in the users table, is therefore not possible.
#s 10: 
#a   : With this, we have defined our first relationship. 
#      A one to one unidirectional relationship between the tables users and addresses.
#      Now we will have a look at how to add some example data with respect to our relationship.
#c   : show-line: {3: 6, 4: 9, 5: 19, 6: 19} data-line: {3: "5-6", 5: "14,15", 6: "16", 7: "24-25", 8: "26", 9: "14,26"}
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///example.db', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = relationship("Address", uselist=False)

    def __repr__(self):
        return 'User(name="%s")' % (self.name)

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    city = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return "Address(city='%s')" % (self.city)
#-#-#-#
#s  1: Creating tables and adding data (unidirectional)
#a   : Creating tables and adding data, unidirectional
#s  2: 
#a   : Similar to what we learned in the chapter basic mapping and setup and installation, 
#      we create the tables we defined, using our engine object and the create_all method.
#      So, calling create_all will create the users table and the addresses table we defined.
#s  3:
#a   : Then we define the session using the session maker function and the session factory.
#s  4:
#a   : Next, we create an instance of the user class. We instanciate the class with name equal to Ed.
#s  5:
#a   : If we print user dot address, we see that it is defined, because it does not throw
#      an error. But so far, the user dot address returns none, because we did not specify the users
#      address.
#s  6:
#a   : To define an address, we instanciate the address class passing city equals London as an argument.
#s  7:
#a   : This address instance can then be set to the user dot address property.
#s  8:
#a   : Printing user dot address will now return the address.
#s  9: 
#a   : Printing address dot id, or address dot user_ID, both will not throw an error, because the properties
#      are defined on the address class. But both properties return the value none. Both values are
#      handled by sql alchemy in the moment we actually save the user to the database.
#s 10: 
#a   : To actually save the user to the database, we first need to add it to the session with session dot add.
#      Then, we can call
#      session dot commit, to actually transfere our changes to the database. This will automatically save
#      the user and the address to the database. It is not neccessary to also add the address
#      to the session. This is automatically handled by sql alchemy.
#      So, after calling seession dot commit, our tables users and addresses, both now have one entry.
#s 11:
#a   : Printing address dot ID, will now return the ID of the address, in this case one. Printing address dot
#      _ ID will return the ID of the user this address belongs. In this case, the address belongs to the user with ID
#      1.
#s 12: 
#a   : Printing user dot id, will show the id of the user, which was also automatically handled by sql alchemy
#      when committing the use to the database. We see that the user has the ID 1. The same value, which was 
#      returned for address dot user _ ID. Of course, we can still get the address of the user, with user dot
#      address. 
#s 13: 
#a   : With that, we now have successfully added one user and one address to the database,
#      where the address can be referenced to the user with help of the user _ ID column.
#      The user _ ID column references the ID of the user which the address 
#      belongs to.
#s 14: 
#a   : We also saw, how to access the users address. Therefore, we can use user dot address. Note, that so far,
#      we only can reference from the user to its address - with user dot address.
#s 15: 
#a   : But, note, that we can not 
#      access the user from an instanciation of an address. 
#      We only can access the ID of the user with address dot user _ ID. But if we want to 
#      have the full user object of the user with ID 1, to get for example the user name, 
#      then we have to execute a 
#      seperate query to query the user object.
#s 16:
#a   : So we can not say, for example, address dot user. This would throw an error.
#      We will see now, how to define a bidirectional relationship. 
#      With a bidirectional relationship, accessing the user object from the address object, 
#      will then be possible.
#c   : show-line: {2: 1, 3: 3, 4: 5, 5: 7, 6: 9, 7: 10, 8: 13, 9: 19, 10:22, 11: 28, 12:34, 13: 34, 14: 34, 15: 34} data-line: {14: "34", 15: "18"}
Base.metadata.create_all(engine)
SessionFactory = sessionmaker(bind=engine)
session = SessionFactory()

user = User(name='ed')
user.address
output_file.write(str(user.address)+ '\n')

address = Address(city="London")
user.address = address

user.address
output_file.write(str(user.address)+ '\n')

address.id
output_file.write(str(address.id)+ '\n')

address.user_id
output_file.write(str(address.user_id)+ '\n')

session.add(user)
session.commit()

address.id
output_file.write(str(address.id)+ '\n')

address.user_id
output_file.write(str(address.user_id)+ '\n')

user.id
output_file.write(str(user.id)+ '\n')

user.address
output_file.write(str(user.address)+ '\n')

# address.user  >> this would throw an error 
#-#-#-#
#s  1: Defining users table and addresses table (bidirectional)
#a   : Defining users table and addresses table bidirectional
#s  2: One to one: One user has one address
#a   : To demonstrate the bidirectional one to one relationship, we will stick to the same example of 
#      a user with one address related to him.
#s  3:
#a   : To define the users and the addresses table, we will need the same imports like before.
#s  4:
#a   : Again, we define our engine object, as well as the base class.
#s  5: 
#a   : Next, we define the user class, almoust in the same way like we did in the unidirectional case. 
#      The only difference here is, that we pass a third argument to the relationship function - back_populates.
#      We set this argument equal to user. This indicates, that a address also will back populate to the user. 
#      That means, that not only a user can 
#      access its address with user dot address, but also, 
#      that a address can reference its user with address dot user.
#s  6: 
#a   : Next, we define the addresses table by defining the address class. 
#      The addresses table will have the same columns like before, the columns ID, of type integer, and city
#      of type string and the foreign key column user _ ID, which holds the id of the user, the address belongs to.
#s  7: 
#a   : For the bidirectional relationship, we now also define the relationship on the addresses table, 
#      similar to how we defined the relationship on the users table.
#      We call the property user 
#      and we use the relationship function to define it. 
#      The relationship function takes the python, in our case the user class, as an first argument
#      because we want to connect this property to the user class.
#s 8: 
#a   : The use list only needs to be defined on the parent class. In 
#      this example, the users table is the parent table and the addresses table is the child table. 
#      Therefore, we only define
#      use list equals to false, on the users class.
#s 9: 
#a   : But we also define back populates and we set it to: address, 
#      which is the property name of the relationship on the user class. With
#      that, we can also access the address on the user instance with user dot address.
#      <break time="3000ms" /> With this, we have defined our bidirectional relationship. 
#      A one to one bidirectional relationship between the tables users and addresses.
#      Now we will have a look at how to add some example data with respect to the bidirectional case.
#c   : show-line: {3: 6, 4: 9, 5: 19, 6: 19} 
#      data-line: {3: "5-6", 5: "16", 6: "24-26", 7: "27", 8: "27", 9: "16,27"}
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///example.db', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = relationship("Address", uselist=False, back_populates="user")

    def __repr__(self):
        return 'User(name="%s")' % (self.name)

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    city = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="address")

    def __repr__(self):
        return "Address(city='%s')" % (self.city)
#-#-#-#
#s  1: Creating tables and adding data
#a   : Creating tables and adding data
#s  2: 
#a   : Here again, we create the tables we defined, using our engine object and the create_all method.
#      Calling create_all will create the users table and the addresses table we defined.
#s  3:
#a   : We again need a session to interact with our database.
#s  4:
#a   : And similarly, we create an instance of an user, passing name equals to Ed, to the constructor.
#s  5:
#a   : Next, we also create an instance of an address, and set it, as the users address, with user dot address
#      equals address.
#s  6: 
#a   : Now, we againn want to save the users and its addres to the datbase. We therefore add it to the session 
#      with session dot add and we can call
#      sesssion dot commit, to actually transfere our changes to the database. This will save
#      the user and the address to the database.
#s  7:
#a   : Printing address dot ID, which we saw, is automatically handled by sql alchemy, 
#      will again return the ID of the address. Because we started with a fresh database, this is again the ID one.
#s  8:
#a   : Printing address dot
#      _ ID will return the ID of the user this address belongs. The address belongs to the user which has also the ID 1.
#      1.
#s  9:
#a   : What is new now is, that we can not only access the users ID, with address dot user_ID, but we can also access the
#      users object from the address, with address dot user.
#s 10:
#a   : To access for example the users name from an address object, we can do this, with address dot user dot name.
#s 11:
#a   : Of course, we can still access the address from an users object, with user dot address. That means, that we
#      now can access the related object in both directions. From the users to the address, and from the address to 
#      the user. <break time="2000ms"/>
#      With that, we have successfully created a bidirectional relationship between the tables users and addresses.
#      We populated data to both tables, and we saw, how we can access the relationships from both directions. From
#      the user to its address and from an address to its users.
#c   : show-line: {2: 1, 3: 3, 4: 5, 5: 8, 6: 11, 7: 14, 8: 17, 9: 20, 10: 23}
Base.metadata.create_all(engine)
SessionFactory = sessionmaker(bind=engine)
session = SessionFactory()

user = User(name='ed')

address = Address(city="London")
user.address = address

session.add(user)
session.commit()

address.id
output_file.write(str(address.id)+ '\n')

address.user_id
output_file.write(str(address.user_id)+ '\n')

address.user
output_file.write(str(address.user)+ '\n')

address.user.name
output_file.write(str(address.user.name)+ '\n')

user.address
output_file.write(str(user.address)+ '\n')
#-#-#-#
output_file.close()
