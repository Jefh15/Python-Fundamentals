# Intro Functions
# Sometimes we copy and paste our code
# import datetime
# print timestamps to see how long sections of code
# take to run

#FUNCTIONS
# Function without args
# By moving the code to a function, you
# reduce rework and the chance of introducing bugs
# when you change the code you had copied
# import the datetime class from datetime library
from datetime import datetime

# Pass the task name as a parameter
def print_time(task_name):
    print(task_name)
    # Now i dont need the extra datetime prefix
    print(datetime.now())
    print()

# Here's another example where the code looks different but 
# we a re doing the same logic over and over
def get_initial(name):
    initial = name[0:1].capitalize()
    return initial

def get_and_print_names():
    first_name = input('Enter your first name: ')
    middle_name = input('Enter your middle name: ')
    last_name = input('Enter your last name: ')
    print('Your initials are: ' + \
            get_initial(first_name) + \
            get_initial(middle_name) + \
            get_initial(last_name)
        )

##################################################################
# MAIN CODE
first_name = 'Susan'
# call the function
print_time('Printed first name')

for x in range(0,10):
    print(x)
#call the function
print_time('Completed for loop')

# call the function
get_and_print_names()
print_time('Completed printing initials')