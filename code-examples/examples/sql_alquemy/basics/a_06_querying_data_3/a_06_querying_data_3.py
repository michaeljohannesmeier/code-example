import os
if os.path.isfile("example.db"):
    os.remove("example.db")
output_filename = os.path.join(os.path.dirname(__file__), "output.txt")
output_file = open(output_filename, "w")
#-#-#-#
"""
# Querying data with filters
## What you will learn  
- Most common filter operations
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

## Common filter operations  
The following code examples shows the most commonly userd operators used in the .filter() method.
<be>
Filter with ==:  
Filters all users with name 'ed'
"""
# ``` python
all_ed_users = session.query(User).filter(User.name == 'ed').all()
all_ed_users
output_file.write(str(all_ed_users)+ '\n')
# Output:
# ```

"""
<br>
Filter with !=:  
Filters all users which name is not 'ed'
"""
# ``` python
all_users_but_ed = session.query(User).filter(User.name != 'ed').all()
all_users_but_ed
output_file.write(str(all_users_but_ed)+ '\n')
# Output:
# ```

"""
<br>
Fitler with like:  
Filters all users with 'ed' somewhere in the name
"""
# ``` python
all_users_containing_ed = session.query(User).filter(User.name.like("%ed%")).all()
all_users_containing_ed
output_file.write(str(all_users_containing_ed)+ '\n')
# Output:
# ```


"""
<br>
Fitler with ilike (case insensitive):
The following example filters all users with 'ed' somewhere in the name 
(independent if 'ed' is written in capital letters or not):
"""
# ``` python
all_users_containing_ed = session.query(User).filter(User.name.ilike("%ed%")).all()
all_users_containing_ed
output_file.write(str(all_users_containing_ed)+ '\n')
# Output:
# ```


"""
<br>
Fitler with in:
The following example filters all users, whhere the user name is in the list ['ed', 'fred', 'jack']:
"""
# ``` python
users_in_list = session.query(User).filter(User.name.in_(['ed', 'fred', 'jack'])).all()
users_in_list
output_file.write(str(users_in_list)+ '\n')
# Output:
# ```


"""
<br>
Fitler with not in:
The following example filters all users, where the user name is not in the list ['ed', 'fred', 'jack']:
"""
# ``` python
users_not_in_list = session.query(User).filter(User.name.notin_(['ed', 'fred', 'jack'])).all()
users_not_in_list
output_file.write(str(users_not_in_list)+ '\n')
# Output:
# ```



#-#-#-#
output_file.close()
