import os
if os.path.isfile("example.db"):
    os.remove("example.db")
output_filename = os.path.join(os.path.dirname(__file__), "output.txt")
output_file = open(output_filename, "w")
#-#-#-#

#s  1: Querying data 3
#a   : Querying data part 3
#s  2: Common filter operations:
#a   : In this section we will have a look at the most common filter operations.
#s  3: - Filter with == operator
#a   : We will have a look at filter with the equality operator
#s  4: - Filter with != operator
#a   : Filter with the negation operator
#s  5: - Fitler with like function
#a   : Filter with the like function
#s  6: - Fitler with case insensitive ilike
#a   : Filter with the case insensitive function, ilike
#s  7: - Fitler with in_ function
#a   : Filter with the in_ function
#s  8: - Fitler with function: notin_
#a   : And finally, filter with the function, not in

#-#-#-#


#s  1: #Prerequisites
#a   : Prerequisites
#s  2:
#a   : Here are all the prerequisites you need in order to run the following examples. If you are not 
#      already familiar with this code, please go back to the sections: setup and installation, and, basic mapping. <break time="2000ms" />.
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
#a   : Then we generated a user class.
#s  5:
#a   : Then we created the actual table in our database.
#s  6:
#a   : Then we created a session.
#s  7: 
#a   : And finally we added four users to our table.
#-#-#-#


#s  1: #Filter with == operator
#a   : Filter with equality operator
#s  2: Filter for equality with == operator in .filter function
#a   : We already used the equality operator with two equal signs. To recap shortly, 
#      let us have a short look at the same example.
#s  3: 
#a   : If we want to filter all users with name equals ed, then we can pass user dot name,
#      equals equals, ed, to the filter function.
#s  4: 
#a   : Printing the result will return a list of users, in our case the list is of length one 
#      and contains only the user ed.
#c   : show-line:{3:1}
users = session.query(User).filter(User.name=='ed').all()
users
output_file.write(str(users)+ '\n')
#-#-#-#


#s  1: #Filter with != operator
#a   : Filter with negation operator
#s  2: Exclude results: use != in filter function
#a   : In case we want to exclude some results and filter onyl users, which name is not equal to ed, 
#      then we do not use equal equal, but, exlamation mark, equal.
#      So here we pass user dot name, exlamation mark, equals, ed, to the filter function.
#s  4: 
#a   : Printing the result will return all users which name is not equal to ed, 
#      so in our case 3 users are returned.
#c   : show-line:{2:1}
users = session.query(User).filter(User.name!='ed').all()
users
output_file.write(str(users)+ '\n')
#-#-#-#


#s  1: #Filter with like function
#a   : Filter with like function
#s  2: Filters all users which have ed somewhere in name: %ed%
#a   : In case we want to filter all users which name contains the word ed,
#      then the method, like, can be used on the name property. So we pass: user
#      dot name, dot like, to the filter function.
#s  3: 
#a   : Printing the result will show two users, ed, and fred, because both user names contain the word ed.
#s  4: 
#a   : For this example, we passed percentage
#      sign, ed, percentage sign to the like function in line 1. The percentage signs are wildcards. 
#      So, in this case, there could be characters before, or, after the word ed.
#s  5: Use ed% in case the name should start with 'ed'
#a   : In case you only want users, which name starts, with ed, then you can pass: ed, percentage sign to the like function.
#      So you omit the first percentage sign.
#s  6: Use %ed in case the name should end with 'ed'
#a   : In case you want that the name ends, with ed, you can pass: percentage sign, ed, to the like 
#      function. So you omit the last percentage sign.
#c   : show-line: {2:1, 3:3, 4:3, 5: 5 } 
#      data-line: {4: "1"}
users = session.query(User).filter(User.name.like("%ed%")).all()
users
output_file.write(str(users)+ '\n')

users = session.query(User).filter(User.name.like("ed%")).all()

users = session.query(User).filter(User.name.like("%ed")).all()
#-#-#-#


#s  1: #Filter with ilike
#a   : Filter with ilike
#s  2: Filters all users which have 'ed' somewhere in name: %ed%
#a   : In case we want to filter all users which name contains the word ed,
#      independent, if ed is written in capital letters or not, then you can use the ilike function.
#      The usage is similar to the one of the like function.
#s  3: 
#a   : So here, we use the ilike function instead of the like function in line 1 to get all users, 
#      which name contains the word ed, independent, if ed is written in capital letters or not.
#s  4:
#a   : The percentage sign wildcard can be used similarly to the examples with the like function.
#      So also here, you can omit the first or the last percentage sign if you want that the name 
#      starts or ends with ed.
#c   : show-line:{2:1} data-line: {3: "1"}
users = session.query(User).filter(User.name.ilike("%ed%")).all()
users
output_file.write(str(users)+ '\n')
#-#-#-#


#s  1: #Filter with in_
#a   : Filter with in_
#s  2: Filter users with a name is in a list
#a   : The following example filters all users, where the user name is in the list: ed, fred, or jack.
#      Therefore, we can use the, in_ function, passing the list of user names as an argument.
#s  3: 
#a   : Printing the result will show two users, ed and fred, because they are in our database and also in
#      the list we passed in line 1 to the in_ function.
#c   : show-line:{2:1}
users = session.query(User).filter(User.name.in_(['ed', 'fred', 'jack'])).all()
users
output_file.write(str(users)+ '\n')
#-#-#-#


#s  1: #Filter with notin_
#a   : Filter with, not in_
#s  2: Filter users with a name is not in a list
#a   : There is also a negation of the function: in_.
#      In this case, we want to filter all users, which names are not in the list ed, fred, and jack.
#      Therefore, we can use the, not in_ function, passing the list of user names an an argument.
#s  3: 
#a   : Printing the result will show two users, wendy and mary, because they are in our database, 
#      but not in the list we passed in line 1 to the not in_ function.
#c   : show-line:{2:1}
users = session.query(User).filter(User.name.notin_(['ed', 'fred', 'jack'])).all()
users
output_file.write(str(users)+ '\n')
#-#-#-#
output_file.close()
