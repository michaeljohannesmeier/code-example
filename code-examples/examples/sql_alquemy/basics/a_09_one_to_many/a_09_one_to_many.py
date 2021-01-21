import os
if os.path.isfile("example.db"):
    os.remove("example.db")
output_filename = os.path.join(os.path.dirname(__file__), "output.txt")
output_file = open(output_filename, "w")
#-#-#-#

#s  1: One to many relationship
#a   : One to many relationship
#s  2: 
#a   : In this chapter, we will have a closer look at the one to many relationship.
#s  3: - Defining users and addresses tables
#a   : Therefore, we will follow the same example like in the one to one relationship.
#      We first define two tables. A users table and an addresses table.
#      We will have a look at how to build a one to many relationship between this two tables.
#s  4: - Creating tables and adding data
#a   : Then, we will create the actual tables and populate the tables with data to see
#      how the data is related in the one to many case.


#-#-#-#
#s  1: Defining users and addresses tables - bidirectional
#a   : Defining users and addresses tables, bidirectional
#s  2: - One user can now have multiple addresses
#a   : Because we have already seen the difference between a unidirectional relationship
#      and a bidirectional relationship, we will only have a look a the bidirectional 
#      case. For that, we will look at the same example as in the one to one relationship,
#      so we will also create a users table and an addresses table. In the one to one
#      example, we assumed, that every user only can have one address related to him. 
#      Now, our business requirements changed, and we want to assume, that every user can
#      have multiple addresses related to him. Therefore, the relationship is one to many,
#      meaning, one user can have many addresses.
#s  3: - Only difference to one to one relationship: uselist=False
#a   : In fact, the one to many example here, is very simmilar to the one to one example
#      which we have seen in the previous chapter.
#      We will see, that the only difference, is the use list argument, passed to the 
#      relationship function defined, on the users class. So lets have a look, at how to
#      create the users and the addresses table.
#s  4: 
#a   : For creating the tables, we need all the following imports. Important for the 
#      relationships are again, line 5 and line 6.
#s  5: 
#a   : Then, we create our base class.
#s  6: 
#a   : Next, we create the python user class, which will be mapped to a database table with tablename users.
#s  7:
#a   : The table should have 2 columns, an ID column of type integer.
#s  8: 
#a   : And a name column of type string.
#s  9:
#a   : Then we define the relationship to our addresses table. Now we want that our addresses
#      property on the users class is of type list, so that we can have multiple addresses
#      related to one user.
#so10: <div class="absolute-bottom-left">One to one: <span class="primary-color">address</span> = relationship("Address", <span class="primary-color">uselist=False</span>, back_populates="user")</div>
#a   : In the one to one relationship, we used the argument use list equals false. Now, in the
#      one to many relationship, we will use, use list equals true, so that multiple addresses
#      can be assigned to a user. Note also, that we called the property addresses, in plural.
#      In the one to one relationship, the property was called address, in singular.
#s 11: 
#a   : We also pass the back_populates argument. It has the same meaning like in the one to one relationship.
#      It means, that the python address class, will have a property called user, and this property
#      will populate back to this user class. So we can also call address dot user, to refere to our user object
#      from an object of type address.
#s 12: 
#a   : Next, we define our address class, wich will define our addresses table.
#      Here we will almost have no changes compared to the one to one relationship. The only 
#      small change will be in the back _ populates argument of the relationship function. We will see this 
#      in a second. Let us first have a look at the properties step by step.
#s 13: 
#a   : The addresses class will have the properties ID and city, mapping 
#      to the columns ID of type integer and city of type string.
#s 14:
#a   : Again, addresses table will persist the relationship to the corresponding user in the colmn user _ ID,
#      which is of type integer and which has the foreign key constrain, that only values from the 
# #    column id of the users table are valid values. 
#      So every row in the addresses table will have a user _ ID, refering to
#      the ID of the user the address belongs to.
#s 15: 
#a   : Then, we define the relationship to the user with the property user, passing the python class
#      we refere to as the first argument and passing back _ populates equals addresses as a second argument.
#      Here is the only small difference to the one to one relationship. Because we called the 
#      relationship on the users class addresses, in plural. So we also pass back _ populates equals to
#      addresses, in plural.
#s 16:
#a   : With that, we have successfully defined our bidirectional many to many relationship between the
#      users table and the addresses table. Now let us have a look, how to populate our tables with some
#      dummy data.
#c   : show-line: {4: 6, 5: 8, 6: 18, 7: 18, 8: 18, 9: 18, 10: 18, 11: 18} 
#      data-line: {4: "5-6", 6: "11", 7: "13", 8: "14", 9: "15", 10: "15", 11: "15", 12: "20-29", 13: "23-24", 14: "25", 15: "26"}
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    addresses = relationship("Address", uselist=True, back_populates="user")

    def __repr__(self):
        return 'User(name="%s")' % (self.name)

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    city = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return "Address(city='%s')" % (self.city)
#-#-#-#
#s  1: Creating tables and adding data - bidirectional
#a   : Creating tables and adding data, bidirectional
#s  2: 
#a   : First, we need to create our tables. Therefore, we again define our engine using an in memory
#      SQ lite database, creating a new file with name example dot db.
#      Then we use this engine, to create our tables, with the create_all method of the base class we defined.
#s  3:
#a   : We also need a session to actually transmit data to our tables.
#      We define the session using the session maker function and the session factory.
#s  4:
#a   : Then, we define a user object with name ed.
#s  5:
#a   : Looking at the addresses of ed, we will see, that now the addresses property returns an empty list. In
#      the case of the one to one relationship, the address property returned none.
#s  6: 
#a   : Let us define two addresses, add 1 with city equals to london, and a second address, add 2 with city equals to 
#      paris.
#s  7:
#a   : Printing, add 1 dot user returns none, because so far, we did not associate the address with the user, or the 
#      other way round. Let us do this now.
#s  8:
#a   : First, we add the first address, add 1, with ed dot addresses dot append, add 1.
#s  9:
#a   : Printing ed dot user will now return the list of addresses related to him.
#s 10:
#a   : Printing add 1 dot user, is now returning the associated user. This means, sql alchemy automatically
#      linked the address to our user.
#s 11:
#a   : We can repeat this step for our second address, with ed dot addresses dot append add 2. Printing
#      ad dot addresses now shows the two addresses, london and paris.
#s 12: 
#a   : This address was also automatically linked to the user
#      ed. Printing ed dot addresses now shows the two addresses which are related to ed. Printing add 2 dot
#      user shows, that also the second address was automatically associated with the user ed.
#s 13:
#a   : Let us now add the user ed to our session, with session dot add, and commit our changes to our database, 
#      with session dot commit. This will save our user and the two addresses related to him to our tables users
#      and addresses.
#s 14:
#a   : As we see, our user was now automatically assigned an ID, the ID 1.
#s 15:
#a   : And the property user _ ID, of our address add 1, was also automatically added to our address.
#      It referes now to the user with ID 1.
#c   : show-line: {2: 2, 3: 5, 4: 7, 5: 10, 6: 13, 7: 15, 8: 17, 9: 20, 10: 22, 11: 27,  12:29, 13: 32, 14: 35} data-line: {}
engine = create_engine('sqlite:///example.db', echo=True)
Base.metadata.create_all(engine)

SessionFactory = sessionmaker(bind=engine)
session = SessionFactory()

ed = User(name='ed')

ed.addresses
output_file.write(str(ed.addresses)+ '\n')

add1 = Address(city="London")
add2 = Address(city="Paris")
add1.user
output_file.write(str(add1.user)+ '\n')

ed.addresses.append(add1)

ed.addresses
output_file.write(str(ed.addresses)+ '\n')
add1.user
output_file.write(str(add1.user)+ '\n')

ed.addresses.append(add2)

ed.addresses
output_file.write(str(ed.addresses)+ '\n')
add2.user
output_file.write(str(add2.user)+ '\n')

session.add(ed)
session.commit()

ed.id
output_file.write(str(ed.id)+ '\n')

add1.user_id
output_file.write(str(add1.user_id)+ '\n')
#-#-#-#
output_file.close()
