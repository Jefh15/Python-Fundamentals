
######################################################################
# DESCRIPTION FILE
# Managing Keys (Sensitive data)
# How to not publish the user and password or 
# PUBLIC KEYS or 
# PRIVATE Keys or
# Github KEYS

# Values from outside of  your application

# Connecting to a database
# Determining the operating system
# Settings wich need to change
# Sensitive data

# USING dotenv
# Store environmental variables in text file
# Don't hardcode
# Don't check sensitive values into source control

# THISSSSSSS I WILL NOT DEPLOY -> ONLY FOR LOCAL PURPOSES ONLY
# .env file
# DATABASE = Sample_Connection_String 

# THIS IS FOR PRODUCTION
# app.py
# from dotenv import load_dotenv 
# import os
# load_dotenv()
# database = os.getenv('DATABASE')
# print(database)

# FINAL NOTES
# Don't hard code sensitive information **EVER**
# Use dotenv for a simple solution
# Add .env to .gitignore

# Consider full encription options
# https://azure.microsoft.com/en-us/products/key-vault

#####################################################################
#IMPORTS
# platform es cross-platform
import os, platform
# sudo apt install python3-dotenv
from dotenv import load_dotenv

#####################################################################
#FUNCTIONS

####################################################################
# MAIN CODE
load_dotenv('DATABASE')
database = os.getenv('DATABASE')
print(database)

# FOR WINDOWS
# os_version = os.getenv('OS')
# FOR LINUX
os_version = platform.system()
# print(platform.system())      # 'Linux'
# print(platform.release())     # kernel version
# print(platform.version())     # detailed version string
# print(platform.platform())    # full descriptive string

print(os_version)