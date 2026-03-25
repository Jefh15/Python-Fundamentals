######################################################################
# DESCRIPTION FILE

# Virtual environments
## By default, packages are installed globally
# Version management becomes a challenge

## Virtual environments can be used to contain 
## and manage package collections
# Really just folder behind the scenes with all your packages

# Python by default install globally the packages
# Virtual environment
# Simply is a folder that has all the code you are gonna need
# to run the application that you are creating
# All that i need will install to that folder and im 
# able to use it

## Creating a virtual environments

# Install virtual environment
#--> pip install virtualenv

# Windows systems
#--> python -m venv <folder_name>

# OSX/ Linux (bash)
#--> sudo apt install python3-virtualenv
#--> virtualenv <folder_name>

## Using virtual environments

# Windows systems
# cmd.exe
# <folder_name>\Scripts\Activate.ps1

# Powershell
# <folder_name>\Scripts\Activate.ps1

# bash shell
# currentfolder/<folder_name>/Scripts/activate

# OSX/Linux (bash)
# Creo el entorno
# python3 -m venv venv
# Now the folder venv in the folder to work was created
# <folder_name>/bin/activate
# in my case to use it just
# source venv/bin/activate
# (venv) crekoj@crekoj-Inspiron-3593:~/Documentos/Jesus/Desarrollo/0 - Learn Python/Cap 35 - Demo Virtual environments$ 

## Installing packages in a virtual environment

#Install an individual package
#--> pip install colorama

#Install from a list of packages
#--> pip install -r requirements.txt

# requirements.txt
#--> colorama

#####################################################################
#IMPORTS


#####################################################################
#FUNCTIONS

##################################################################
# MAIN CODE
