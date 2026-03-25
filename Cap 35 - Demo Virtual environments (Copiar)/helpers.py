######################################################################
# DESCRIPTION FILE

# Demo Virtual environments

#####################################################################
#IMPORTS
from colorama import init, Fore

#####################################################################
#FUNCTIONS

def display(message, is_warning=False):
    if is_warning:
        print(Fore.RED + message)
    else:
        print(Fore.BLUE + message)



##################################################################
# MAIN CODE