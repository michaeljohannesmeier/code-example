import os
if os.path.isfile("example.db"):
    os.remove("example.db")
output_filename = os.path.join(os.path.dirname(__file__), "output.txt")
output_file = open(output_filename, "w")

#-#-#-#

#s  1: #Querying data 2
#a   : Querying data 2
#s  2: 
#a   : In this section we will have a deeper look into how to query data with further options.
#s  3: - Query one specific element with exception
#a   : We will see how to query a specific element with exceptions
#s  4: - Query one specific element without exception if no element could have been found
#a   : How to query one specific element without exception if no element could have been found.
#s  5: - Query with limit and offset
#a   : How to limit our queries and how to use an offset
#s  6: - Return ordered queries
#a   : And how to return ordered queries

#-#-#-#

#s  1: #Prerequisites
#a   : Prerequisites
#s  2:
#a   : Here are all the prerequisites you need in order to run the following examples. If you are not 
#      already familiar with this code, please go back to the previous sections. <break time="2000ms" />.
#c   : show-line: {2: 16, 3: 21, 4: 21, 5: 21, 6: 24} 
#      data-line: {3: "6", 4: "9-19", 5: "21", 6: "23-24", 7: "26-32"}
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///example.db', echo=True)

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return 'User(name="%s")' % (self.name)

Base.metadata.create_all(engine)

SessionFactory = sessionmaker(bind=engine)
session = SessionFactory()

user = User(name='ed', fullname='Ed Jones', nickname='eddy', age=64)
session.add(user)
session.add_all([
    User(name='wendy', fullname='Wendy Williams', nickname='windy', age=17),
    User(name='mary', fullname='Mary Contrary', nickname='mary', age=34),
    User(name='fred', fullname='Fred Flintstone', nickname='freddy', age=29)])
session.commit()
#s  3:
#a   : To recap quickly what we did so far. We first generated an engine object.
#s  4:
#a   : Then we generated a user class defining the table name and the table columns.
#s  5:
#a   : After defining the mapper class, the create _ all method created the actual table in our database.
#s  6:
#a   : Further, we created a session with the help of the session maker function and the session factory.
#s  7: 
#a   : And finally we used this session to add four users to our table.
#-#-#-#



#s  1: #Querying one specific element with exeception
#a   : Querying one specific element
#s  2: Find one specific element with .one()
#a   : If you want to find one specific element, the dot one method can be used.
#      In this example, we want to query a user which name is ed and which age is 64. After the filter method,
#      the dot one method is now used to only query one specific element.
#s  3: 
#a   : If we print our result, we can see that we recieved the user with name ed and age 64.
#s  4:
#a   : If we would like to find a user with name ed and age of 20, then, the execution of line 6 would 
#      throw an error, because no user with name ed and age 20 could have been found in our users table.
#      The .one method will throw an exception if not exactly one element was found, 
#      that means, if none, or more than one element was found.
#c   : show-line: {2: 1, 3: 5} 
#      data-line: {4: "8"}
user = session.query(User).filter(User.name=='ed', User.age==64).one()
user
output_file.write(str(user)+ '\n')
user.age
output_file.write(str(user.age)+ '\n')

try:
    user_ed = session.query(User).filter(User.name=='ed', User.age==20).one()
except Exception as e:
    print("No user found")
#-#-#-#


#s  1: #Query one specific element without exception if no element could have been found
#a   : Querying one specific element without exception if no element could have been found
#s  2: - User .one_or_none() to query one specific element
#a   : If exactly one element should be queried from the database, without throwing an exception 
#      in case no element could have been found, then the dot one or none method can be used.
#s  3: - No exception is thrown, if no element was found
#a   : So this method will not throw an error, if no element could be found
#s  4: - Throws error, if multiple elements could have been found
#a   : But it will throw an error, if multiple elements could have been found
#s  5: 
#a   : In this example, we again want to query a user with name ed, and age of 64. This time, we use the
#      one or none method.
#s  6:
#a   : Executing this line and printing the result will show us the user ed.
#s  7:
#a   : If there would have been more than one user with name ed and age 64 in our database, 
#      then, then execution of line 2 whould have been thrown an exception which we handle in line 5 and 6.
#s  8:
#a   : Next, imagine we would like to query a user with name ed and age 63. Because we do not have
#      any user with name ed of age 63, no user will be found.
#s  9: 
#a   : Printing the result would return none. So the execution of line 9 would not throw an exception, because no user was found.
#      But keep in mind, the method dot one or none will do throw an error, if more then one element could be 
#      found.
#s 10:
#a   : So lines 2 and 9 would both throw an error, if more than one element would have been found.
#      That is why, the method one or none should therefore always be used inside a try except block.
#c   : show-line: {5: 2, 6: 6, 7: 9} 
#      data-line: {6: "3-4", 7: "2, 5-6", 8: "9", 9: "9-11", 10: "2,9"}
try:
    user_ed = session.query(User).filter(User.name=='ed', User.age==64).one_or_none()
    user_ed
    output_file.write(str(user_ed)+ '\n')
except Exception as e:
    print("Multiple users have been found")

try:
    user_ed = session.query(User).filter(User.name=='ed', User.age==63).one_or_none()
    user_ed
    output_file.write(str(user_ed)+ '\n')
except Exception as e:
    print("Multiple users have been found")
#-#-#-#


#s  1: #Query with limit and offset
#a   : Querying with limit and offset
#s  2: - Use the python list slicing syntax to limit the query
#a   : In case not all elements should be returned from the database, a limit can be specified using 
#      python list slices - so using the square brakets.
#      For example, if only the first two elements should be returned, then the slicing,
#      open square bracket, double point, 2, closed square bracket can be added after the dot all method.
#s  3:
#a   : If we print this result, we see that we now get back an list of only 2 users, ed and wendy.
#s  4: - List slicing can also be used to skip elements
#a   : Similarly, for skipping elements, the python list slicing can also be used. This is
#      usually called querying with offset. For example, to skip the first element, the slicing, 
#      open square bracket, 1, double point, closed square bracket can be added after the dot all method.
#s  5:
#a   : Printing this, will return only 3 users. The first user was now skipped.
#c   : show-line: {2: 1, 3: 3, 4: 5}
all_users_with_limit = session.query(User).all()[:2]
all_users_with_limit
output_file.write(str(all_users_with_limit)+ '\n')

all_users_with_offset = session.query(User).all()[1:]
all_users_with_offset
output_file.write(str(all_users_with_offset)+ '\n')
#-#-#-#

#s  1: #Ordered queries
#a   : Ordered queries
#s  2: - User oder_by to order results
#a   : To order the data we want to query, the order_by function can be used. It takes one or more columns 
#      as arguments by which the data should be ordered. If we want to order for example by age, 
#      then we can add the dot order by method and pass user dot age to it. 
#s  3: 
#a   : Printing this will return all 4 users, ordered by age. So wendy has the smallest age and 
#      ed has the biggest age. 
#s  4: - Default ordering is ascending - use .desc to order descending
#a   : By default, the order is ascending. That means, for numbers, the ordering goes from the smallest to 
#      the biggest number, and for characters the ordering goes from a to z.
#      For ordering descending, it is possible to use the DESC function, which can be imported from sqlalchemy.
#s  5: 
#a   : Printing this will show us all users, ordered descending by age. This time, the order is skipped,
#      ed is the first user and wendy is the last user in the list.
#c   : show-line: {2: 1, 3: 3, 4: 6}
by_age_ordered_users = session.query(User).order_by(User.age).all()
by_age_ordered_users
output_file.write(str(by_age_ordered_users)+ '\n')

from sqlalchemy import desc
by_age_ordered_desc = session.query(User).order_by(User.age.desc()).all()
by_age_ordered_desc
output_file.write(str(by_age_ordered_desc)+ '\n')
#-#-#-#
output_file.close()
