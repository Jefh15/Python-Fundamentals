# Conditional handling

# Symbol | Operation
# > | Greather than
# < | Less than
# >= | Greather than or equal to
# <= Less than or equal to
# == | is equal to
# != | is not equal to 

# Your code needs the ability to take different
# actions based on different conditions
#price = 3 
#if price >= 1.00:
#    tax = .07
#    print(tax)

# You can add a default action using else
#price = 3
#if price >= 1.00:
#    tax = .07
#else:
#    tax = 0
#print(tax)

#Be careful when comparing strings
# string coparisons are case sensitive
#country = 'CANADA'
#if country == 'canada':
#    print('Oh look a Canadian')
#else:
#    print('You are not from Canada')

# Use string functions to make 
# case insensitive comparisons
country = 'CANADA'
if country.lower() == 'canada':
    print('Oh look a Canadian')
else:
    print('You are not from Canada')