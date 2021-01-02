import os
if os.path.isfile("example.db"):
    os.remove("example.db")
output_filename = os.path.join(os.path.dirname(__file__), "output.txt")
output_file = open(output_filename, "w")
#-#-#-#
"""
# Querying data with further options
## What you will learn  
- Query one specific element  
- Query with limit and offset  
- Query and order data
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

## Query one specific element (with exeception)
If you want to find one specific element (row) in the database, the .one() methods can be used:
"""
# ``` python
user_ed = session.query(User).filter(User.name=='ed', User.age==64).one()
user_ed
output_file.write(str(user_ed)+ '\n')
# Output:

# This will throw an exception because no user with name ed and age 20 exists in the database:
# user_ed = session.query(User).filter(User.name=='ed', User.age==64).one()
# ```
"""
The .one() method will throw an exception if not exactly one element was found in the database (if none ore more than one element was found).
"""


"""
<br>

## Query one specific element (without exception if no element could have been found)
If exactly one element should be queried from the database, without throwing an exception in case no element could have been found, 
then the .one_or_none() method can be used:
"""
# ``` python
user_ed = session.query(User).filter(User.name=='ed', User.age==64).one_or_none()
user_ed
output_file.write(str(user_ed)+ '\n')
# Output:

user_ed = session.query(User).filter(User.name=='ed', User.age==63).one_or_none()
user_ed
output_file.write(str(user_ed)+ '\n')
# Output:
# ```
"""
The method .one_or_none() throws an error if more then one element could be found in the database.
"""




"""
<br>

## Query with limit and offset
In case not all elements should be returned from the database, the limit can be written with pythons array slices.
For example, if only two elements should be returned, used: `[:2]`.
"""
# ``` python
all_users_with_limit = session.query(User).all()[:2]
all_users_with_limit
output_file.write(str(all_users_with_limit)+ '\n')
# Output:
# ```

"""
Similarly, for skipping elements (querying data with an offset), also the python array slice can be used, for example: `[1:]`
"""
# ``` python
all_users_with_offset = session.query(User).all()[1:]
all_users_with_offset
output_file.write(str(all_users_with_offset)+ '\n')
# Output:
# ```


"""
<br>

## Query and order data
To order data, the order_by function can be used. 
It takes the tables column(s) as argument(s) by which the data should be ordered:
"""
# ``` python
by_name_ordered_users = session.query(User).order_by(User.name).all()
by_name_ordered_users
output_file.write(str(by_name_ordered_users)+ '\n')
# Output:

by_age_ordered_users = session.query(User).order_by(User.age).all()
by_age_ordered_users
output_file.write(str(by_age_ordered_users)+ '\n')
# Output:
# ```
"""
<br>
By default, the order is ascending (for numers: from the smallest to the biggest, for characters: from a to z).
For ordering descending it it possible to use the .desc() function:
"""
# ``` python
by_age_ordered_asc = session.query(User).order_by(User.age).all()
by_age_ordered_asc
output_file.write(str(by_age_ordered_asc)+ '\n')

from sqlalchemy import desc
by_age_ordered_desc = session.query(User).order_by(User.age.desc()).all()
by_age_ordered_desc
output_file.write(str(by_age_ordered_desc)+ '\n')
# Output:
# ```

#-#-#-#
output_file.close()
