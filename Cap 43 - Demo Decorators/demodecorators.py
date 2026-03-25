
######################################################################
# DESCRIPTION FILE
# Demo Decorators 

#####################################################################
#IMPORTS

#####################################################################
#FUNCTIONS

####################################################################
# MAIN CODE
# HOW TO CREATE A DECORATOR
def logger(func):
    def wrapper():
       # First log
       print('Logging execution')
       # Execute the function
       func()
       # Last log
       print('Done logging')
    return wrapper

@logger
def sample():
    print('-- Inside sample function')

sample()