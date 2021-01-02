
#-#-#-#
"""
# Installation and Setup
## What you will learn  
- Creating a virtual environment  
- Installing sql-alchemy  
- Verifying the installation  
- Create an engine object to connect to the database  
</br>

## Generate virtualenv
Generate a new folder called `sql_alchemy` and cd into it  
Generate a virtual environment with `python -m virtualenv venv` (if you dont have virtualenv installed already, run `pip install virtualenv`)  
Activate the virtual environment with `source venv/Scripts/activate`
"""

"""
</br>

## Install sql alchemy
"""
# ``` python
pip install sqlalchemy
# ```

"""
</br>

## Verify installation
Check that you have sql alchemy installed successfully.

"""
# ``` python
import sqlalchemy
sqlalchemy.__version__ 
>>> 1.3.0
# ```
"""
</br>

## Connect to Database with engine
SQLite database example.db:
"""
# ``` python
from sqlalchemy import create_engine
engine = create_engine('sqlite:///example.db', echo=True)
# ```
"""
echo=True enables logging
"""
#-#-#-#
