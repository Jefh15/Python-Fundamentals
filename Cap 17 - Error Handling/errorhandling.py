# Error types

# Syntax errors
# This code won't run at all
#x = 42
#y = 206
# SyntaxError: expected ':'
#if x == y
#    print('Success!!')

# Runtime errors
#This code will fail when run
#x = 42
#y = 0
# ZeroDivisionError: division by zero
#print(x / y)

#Catching runtime errors
#x = 42
#y = 0
#try:
#    print(x / y)
#except ZeroDivisionError as e:
#    print('Sorry, something went wrong')
#except:
#    print('Sorry really went wrong')
#finally:
#    print('This always runs or success or failure')
# Some final words on try/except/finally
# Not used to find bugs
# Debugging, not error handling
# You don't have to catch all errors
# Let it bubble up
# Someone else with deal with it
# The application will crash
# Sometimes, this exactly what you want to happen

# Logic errors
# This code won't run at all
x = 206
y = 42
if x < y:
    print(str(x) + ' is greater than ' + str(y))