######################################################################
# DESCRIPTION FILE

# Modules and packages

# What's a module?
# A Python file with functions, classes and other components

# Why use modules?
# Break code down into reusable structures
#############################
# Packages
# What are packages
# Published collections of modules

# How do i find packages ?
# https://pypi.org/

##########################
# Installing packages (up to date version not speccific version)

# Install an individual package
#########pip install colorama

# Install from a list of packages
########pip install -r requirements.txt

# requirements.txt
########colorama

#####################################################################
#IMPORTS
# Use a module
# 3 Ways to importing a module

#import module as namespace
import helpers # type: ignore

#import all into current namespace
from helpers import * # type: ignore

#import spacefic items into current namespace
from helpers import display # type: ignore


#####################################################################
#FUNCTIONS

##################################################################
# MAIN CODE
# first import
helpers.display('Not a warning')
# second import
display('Not a warning')
# third import
display('Not a warning')