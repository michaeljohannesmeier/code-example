
#-#-#-#

#: #Installation and Setup
#a: In this part we will talk about the installation and the setup
#: What you will learn
#a: Here is what you will learn
#: - Creating a virtual environment
#a: You will learn how to create a virtual environment
#: - Installing sql-alchemy
#a: How to install sql alchemy
#: - Verifying the installation
#a: How to verify the installation
#: - Create an engine object to connect to the database
#a: And finally you will learn how to create an engine object to connect to the database

#-#-#-#

#: #Generate virtualenv
#a: Generate a virtual environment
#: Generate a new folder called `sql_alchemy` and cd into it
#a: Generate a new folder called sql alchemy and open that folder
#: Generate a virtual environment with `python -m virtualenv venv` (if you dont have virtualenv installed already, run `pip install virtualenv`)  
#a: Inside this folder, run python -m virtualenv venv to create a virtual environment
#: Activate the virtual environment with `source venv/Scripts/activate`
#a: Activate the environment with source activate

#-#-#-#

#: #Install sql alchemy
#a: Install sql alchemy
#: Install sql alchemy from the command line with the following command:
#a: From the command line, run pip install sql alchemy to install sql alchemy
#c: show-line: {2: 1}
pip install sqlalchemy

#-#-#-#

#: #Verify installation
#a: Verify the installation
#:Check that you have sql alchemy installed successfully.
#a: After the installation you should be able to import sql alchemy and see the version with this code
#c: show-line: {2: 1, 3:2}
import sqlalchemy
sqlalchemy.__version__ 
#: >>> 1.3.0
#a: You should see the version number

#-#-#-#

#: #Connect to Database with engine
#a: Connect to the database
#: SQLite database example.db:
#a: Now that sql alquemy is installed, we have to connect to it with the following code
#c: show-line: {2: 1, 3:2}
from sqlalchemy import create_engine
engine = create_engine('sqlite:///example.db', echo=True)
#: echo=True enables logging
#a: echo equals true means that logging is enabled

#-#-#-#
