
######################################################################
# DESCRIPTION FILE
# Decorators 
# How this works and how this operate
# 
# Programming components
# Objects
# Nouns
# Data constructs
# Functions/Methods
# Verbs
# Actions

# Decorators
# Adjectives
# Add additional functionality to code
# Common in frameworks
# Django
# Flask

# Used for add functionality to own code

# EXAMPLE with @route('/api/products') -> when someone 
# navigate to https://myserver/api/products load the method
# get_products
# using a decorator
# Snippet from Flask
# register https://myserver/api/products
# @route('api/products')
# def get_products:
    # code to list from database
    # pass

#############################
# HOW TO CREATE A DECORATOR
# def logger(func):
#   def wrapper():
#       print('Logging execution')
#       func()
#       print('Done logging')
#   return wrapper

# @logger
# def sample():
#   print('-- Inside sample function')

# sample()

#####################################################################
#IMPORTS

#####################################################################
#FUNCTIONS

####################################################################
# MAIN CODE
