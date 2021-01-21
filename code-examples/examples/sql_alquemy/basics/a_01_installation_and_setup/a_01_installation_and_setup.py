
#-#-#-#

#s  1: #Installation and Setup of SQL Alchemy
#an  : Installation and setup of sql alchemy
#sn 2: - Create a virtual environment
#a   : In this video we will first, create a virtual environment.
#sn 3: - Installing sql alchemy
#a   : Then we will install sql alchemy into this virtual environment.
#sn 4: - Verifying the installation
#a   : After we installed sql alchemy we will shortly verify that the installation was successful.
#sn 5: - Create an engine object to connect to the database
#a   : And finally we will create an engine object, which will be later used to connect to the database.

#-#-#-#

#s  1: #Generate virtualenv
#an  : Generating a virtual environment
#s  2: - Generate a new folder called `sql_alchemy` and open that folder
#an  : First we will generate a folder which will hold all our source code. So generate a new folder called sql alchemy 
#      and open that folder
#s  3: - Generate a virtual environment with `python -m virtualenv venv`
#an  : Inside this folder we will create the virtual environment. To do so, open a terminal inside this folder and 
#      run python minus m virtualenv venv.
#      If you dont have virtualenv already installed, run pip install virtualenv from the commandline first.
#s  4: - Activate the virtual environment with `source venv/Scripts/activate` on Windows or `source venv/bin/activate` on unix 
#      based systems
#an  : After the creation of the virtual environment we have to activate it. This can be done with the command 
#      source activate. <break time="1000ms"/> The activate script is located in our v env folder and there in the folder - Scripts - on Windows machines, 
#      or in the folder - bin - on unix based systems.
#      After we have now successfully activated our virtual environment, everything we install 
#      will be installed into this environment. <break time="2000ms"/> Next we will see how to install sql alchemy into this 
#      virtual environment.

#-#-#-#

#sn 1: #Install sql alchemy
#a   : Installing sql alchemy
#sn 2: From the command line run:
#a   : To now install sql alchemy in our virtual environment, run pip install sql alchemy 
#      from the command line. This will install the latest version of sql alchemy into our virtual environment.
#c   : show-line: {2: 1}
pip install sqlalchemy
#-#-#-#

#sn 1: #Verify installation
#a   : Verify the installation
#sn 2: Check that you have sql alchemy installed successfully.
#a   : After the installation you should be able to import sql alchemy and run sql alchemy, dot, double underscore, version, 
#      double underscore:
#c   : show-line: {2: 2}
import sqlalchemy
sqlalchemy.__version__ 
#>>> 1.3.0
#sn 3:
#a   : Executing this, should show you the version number of sql alchemy. At the time of recording, this was 1.3.0.

#-#-#-#

#sn 1: #Create engine object
#a   : Creating an engine object
#sn 2: Sql alchemy engine will be used to connect to databse
#a   : In order that sql alchemy can later connect to our database, it needs a so called engine object. 
#      To create such an engine, we can use the function create_engine.
#      The function takes an connection string as the first argument.
#      For the following examples we will use a SQ lite database. A SQ lite database will be a simple file on our file system.
#      The connection string for a SQ lite database can be specified as: SQ lite, double point, 
#      then a tripple slash and then the name of our database, in our case example dot db. 
#      Whith this connection string, sql alchemy will later create a file called example dot db which will serve as our database.
#c   : show-line: {2: 2} data-line: {2: "2"}
from sqlalchemy import create_engine
engine = create_engine('sqlite:///example.db', echo=True)
#sn 3: echo=True enables logging
#a   : The create engine function also takes another argument - echo. Echo can be set to true to enable log messages.
#      <break time="2000ms"/> Creating the engine did not create any database or any tables so far.
#      We will see in the next chapter how to use this engine to create our database tables with sql alchmey.

#-#-#-#
