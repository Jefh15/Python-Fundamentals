
######################################################################
# DESCRIPTION FILE
# Demo Managing Keys 

#####################################################################
#IMPORTS
from dotenv import load_dotenv
import os
#####################################################################
#FUNCTIONS

####################################################################
# MAIN CODE
load_dotenv()
user = os.getenv('USER')
password = os.getenv('PASSWORD')
constringdb = os.getenv('CON_STRING_DB')

# print the password from .env
print(user)
print(password)
print(constringdb)