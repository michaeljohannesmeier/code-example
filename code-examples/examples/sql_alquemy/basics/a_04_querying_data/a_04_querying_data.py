import os
if os.path.isfile("example.db"):
    os.remove("example.db")
output_filename = os.path.join(os.path.dirname(__file__), "output.txt")
output_file = open(output_filename, "w")
#-#-#-#



#s  1: Querying data
#a   : Querying data from the database
#s  2: Query data from the database  
#a   : In this section, we will have a look at how to query data from the users table in our database.
#s  3: - Short recap (prerequisites)
#a   : Therefore, we will shortly recap what we did so far.
#s  4: - Query all elements from the database (all rows and all columns)
#a   : Then we will have a look how to query all elements from our users table.
#s  5: - Query specific columns (specific colums, all rows)
#a   : How to query only specific columns
#s  6: - Query with filter (all columns, only specific rows)
#a   : How to use the filter method to filter by row
#s  7: - Query specific columns and specific rows
#a   : How to query specific columns and specific rows
#s  8: - Query first element
#a   : And how to query only the first element found in the table.
#-#-#-#

#s  1: #Prerequisites
#a   : Prerequisites
#s  2:
#a   : Here are all the prerequisites you need in order to run the following examples. If you are not 
#      already familiar with this code, please go back to the previous sections. <break time="2000ms" />.
#c   : show-line: {2: 16, 3: 21, 4: 21, 5: 21, 6: 21, 7: 24} 
#      data-line: {3: "6", 4: "9-19", 5: "16", 6: "21", 7: "23-24", 8: "26-32"}
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
#a   : In contrast to the previous example, this users table has one additional column, 
#      the column - age, which is of type integer.
#s  6:
#a   : After defining the mapper class, the create _ all method created the actual table in our database.
#s  7:
#a   : Further, we created a session with the help of the session maker function and the session factory.
#s  8: 
#a   : And finally we used this session to add four users to our table using the methods - session add  
#      and session add _ all. The 4 users we added are - ed, wendy, mary and fred. 
#      The actual transaction to the database took place 
#      when session dot commit was called in line 32.
#-#-#-#



#s  1: #Query all elements from the database (all rows and all columns)
#a   : Querying all elements from the database
#s  2: - Use session.query() to query data
#a   : To query data from the database, the dot query method of the session object 
#     can be used. This method takes the mapper class of the table you want to query as an argument. 
#     In our case we want to query the users table, so we pass the user class to the dot query method.
#s  3: - Use all() method to query all rows
#a   : This construct can then be further chained, for example with the dot all 
#      method to query all users from the database.
#s  4: 
#a   : Printing all users will then return our 4 users in the database in 
#      form of the string representation which we defined in our user class.
#c   : show-line: {2: 1, 3: 1}
all_users = session.query(User).all()
all_users
output_file.write(str(all_users) + "\n")
#-#-#-#


#s  1: # Query specific columns (specific colums, all rows)
#a   : Querying specific columns from the database
#s  2: 
#a   : In the previous example we queried all columns and all rows from the users table
#      using the method dot all.
#s  3: Pass column name of mapper class to .query to specify columns
#a   : To select only specific columns, it is possible to pass the column names as arguements to the 
#      query function. In this example, we pass user dot name and user dot nickname to the query function
#      in order to only query the names and the nicknames.
#s  4: 
#a   : The dot all method will always return a list of objects. 
#      We can access the first user of the all _ users list with all _ users 0.
#s  5: 
#a   : Printing the name of the first user will return ed.
#s  6: 
#a   : But printing the age of the first user would throw an error, because we 
#      did not query the column age.
#      We only queried the name and the nickname column.
#c   : show-line: {2: 1, 3: 3, 4: 4, 5: 7}
all_users_all_columns = session.query(User).all()

all_users = session.query(User.name, User.nickname).all()
first_user = all_users[0]

first_user.name
output_file.write(str(first_user.name) + "\n")

# first_user.age
# >>> AttributeError: 'result' object has no attribute 'age'
#-#-#-#


#s  1: #Query with filter (all columns, only specific rows)
#a   : Querying specific rows with the filter method
#s  2: - User .filter() method to filter rows
#a   : In order to query only specific rows in our table, the query method of the session object 
#      can be chained with the filter method to filter by one or more conditions.
#      For example, to query only the users, which name equals ed, pass user dot name equals equals ed to the
#      filter function. Then add the dot all method to query all filtered rows.
#s  3: 
#a   : When executing this, the result will be a list of users, which all have the name ed. 
#      In our small example table, we only have 
#      one user with name ed. Therefore, the list is of length one.
#s  4: 
#a   : It is also possible to add multiple conditions to the filter function. In this example, we want to 
#      query all users with name add, which age is smaller than 30.
#s  5:
#a   : Printing our result will return an empty list, because we only have one user with name ed. And the age of
#      this user is 64, so it is not smaller than 30.
#s  6: 
#a   : As an alternative syntax, the example can also be written with multiple filter methods chained together.
#      In line 9, the filter method is called two times, one time with user dot name, and one time with user dot age.
#      Line 5 and line 9 are equivalent, they will return the exact same result, in our case a empty list.
#      It does not matter if you pass all your conditions into one filter method or if you call the filter method
#      multiple times.
#c   : show-line: {2: 1, 3: 3, 4: 5, 5: 7} 
#      data-line: {6: "5,9"}
all_users_with_name_ed = session.query(User).filter(User.name=='ed').all()
all_users_with_name_ed
output_file.write(str(all_users_with_name_ed) + "\n")

users = session.query(User).filter(User.name=='ed', User.age<30).all()
users
output_file.write(str(users) + "\n")

users_2 = session.query(User).filter(User.name=='ed').filter(User.age<30).all()
users_2
output_file.write(str(users_2) + "\n")

#-#-#-#


#s  1: #Query specific columns and specific rows
#a   : Querying specific columns and specific rows
#s  2: - Pass column to .query method and use .filter to query specific colums and specific rows
#a   : Now we can combine what we learned so far. We can pass the columns we want to query to the query method 
#      in order to query only specific columns. And we can additionally use the dot filter method to query only 
#      specific rows. For example, to get only the name and the age column of all users which name equals ed, 
#      we pass user dot name and user dot age to the query method and we then chain the 
#      filter method with the condition - user dot name equals equals ed
#s  3: 
#a   : Printing the users name will return ed.
#s  4:
#a   : Printing the users age will return 64, which is the age of the user with name ed. 
#      Printing for example, user dot nickname, would again
#      throw an exception, because only name and age are defined on the user instance.
#c   : show-line: {2: 1, 3: 6}
users = session.query(User.name, User.age).filter(User.name=='ed').all()

uses = users[0]

user.name
output_file.write(str(user.name) + "\n")

user.age
output_file.write(str(user.age) + "\n")
#-#-#-#


#s  1: #Query first element
#a   : Querying only the first element
#s  2: Use .first method to get only first element
#a   : In order to query only the first row which can be found in the table, the query method of the session 
#      object can be chained with the dot first method.
#s  3:
#a   : In this case, we did not recieve a list of users, but only one user element.
#s  4: 
#a   : To see the name of the user we queried, we can therefore print first _ users dot name
#      directly on our result.
#c   : show-line: {2: 1, 3: 3}
first_user = session.query(User).first()
first_user
output_file.write(str(first_user) + "\n")

first_user.name
output_file.write(str(first_user.name) + "\n")
#-#-#-#


output_file.close()
