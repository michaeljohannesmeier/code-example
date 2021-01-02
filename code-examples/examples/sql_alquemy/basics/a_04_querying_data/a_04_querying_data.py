import os
if os.path.isfile("example.db"):
    os.remove("example.db")
output_filename = os.path.join(os.path.dirname(__file__), "output.txt")
output_file = open(output_filename, "w")
#-#-#-#


"""
# Querying data
## What you will learn  
- Query data from the database  
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
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                            self.name, self.fullname, self.nickname)
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
# ```

#-#-#-#

"""
<br>

## Query all elements from the database (all rows and all columns) 
To query data from the database, the query method of the session object 
can be used. This method takes the python class (which is mapped to the 
database table) as an argument.
This construct can then be further chained, for example with the .all() 
method to query all users from the database:
"""
# ``` python
all_users = session.query(User).all()
all_users
output_file.write(str(all_users) + "\n")
# Output:
# ```

"""
<br>

## Query specific columns (specific colums, all rows)
The example above with `session.query(User)` queries all columns. To select only specific columns,
pass the column names as arguements to the query function like: `session.query(User.name, User.fullname).all()`.
"""
# ``` python
all_user_names = session.query(User.name).all()
all_user_names
output_file.write(str(all_user_names) + "\n")
# Output:

all_user_names_and_nicknames = session.query(User.name, User.nickname).all()
all_user_names_and_nicknames
output_file.write(str(all_user_names_and_nicknames) + "\n")
# Output:
# ```


"""
<br>

## Query with filter (all columns, only specific rows)
The query method of the session object can be chained with the .filter()
method to filter the database by one or more conditions:
"""
# ``` python
all_users_with_name_ed = session.query(User).filter(User.name=='ed').all()
all_users_with_name_ed
output_file.write(str(all_users_with_name_ed) + "\n")
# Output:

all_users_with_name_ed_under_30 = session.query(User).filter(User.name=='ed', User.age<30).all()
all_users_with_name_ed_under_30
output_file.write(str(all_users_with_name_ed_under_30) + "\n")
# Output:
# ```
"""
`session.query(User).filter(User.name=='ed', User.age<30).all()` can be also written as `session.query(User).filter(User.name=='ed').filter(User.age<30).all()` - both statements are equal. 
Because there are no users with name 'ed' and a age under 30 years, both examples return an empty list.
"""


"""
<br>

## Query specific columns and specific rows
Combine the arguemnts in the query methods and the .filter method to specify specific columns and filter by row.
For example, to get only the ages of all users with name ed use:
"""
# ``` python
ages_of_all_users_with_name_ed = session.query(User.age).filter(User.name=='ed').all()
ages_of_all_users_with_name_ed
output_file.write(str(ages_of_all_users_with_name_ed) + "\n")
# Output:
# ```



"""
<br>

## Query first element
The query method of the session object can be chained with the .first()
method to query only the first user from the database:
"""
# ``` python
first_user = session.query(User).first()
first_user
output_file.write(str(first_user) + "\n")
# Output:
# ```




#-#-#-#
output_file.close()
