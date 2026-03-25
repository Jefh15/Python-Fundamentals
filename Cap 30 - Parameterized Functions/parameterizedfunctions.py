# Function parameters and multiparameters

#FUNCTIONS
# Here's another example where the code looks different but 
# we a re doing the same logic over and over
# func_name(param1, param2)
# You can specify a default value for a parameter
# like -> force_uppercase=True
def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1].lower()
    return initial


def get_and_print_first_and_last_name():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    # get_initial(param1, if the param2 was set it to True 
    # can be typed optional)
    
    # you can also assign the values to parameters
    # by name when you call the function
    
    # you can also assign the values to parameters
    # by name when you call the function
    #print('Your initials are: '+ \
    #      get_initial(name=first_name, force_uppercase=True) + \
    #      get_initial(name=last_name, force_uppercase=True))


    # get_initial(param1, param2)
    print('Your initials are: '+ \
          get_initial(first_name, False) + \
          get_initial(last_name, True))

# Using the named notation when calling
# functions makes your code more readable
def error_logger(error_code, error_severity, log_to_db, \
                 error_message, source_module):
    print('oh no error: ' + error_message)
    #imagine code here that logs our error to a database or file



# MAIN CODE

# call the function
get_and_print_first_and_last_name()

fir_number = 10
sec_number = 5
if fir_number > sec_number:
    # unreadable
    #error_logger(45,1, True,
    #             'Second number grater than first',
    #             'my_math_method')
    
    #readable code
    error_logger(error_code=45,error_severity=1, log_to_db=True,
                 error_message='Second number grater than first',
                 source_module='my_math_method')