# Handling multiple conditions

# You may need to check multiple conditions 
# to determine the correct action
# Note: this works with exists more elegant way to do
#province = input('Enter the name of your home country: ')
#if province.capitalize() == 'Alberta':
#    tax = 0.05
#if province.capitalize() == 'Nunavut':
#    tax = 0.05
#if province.capitalize() == 'Ontario':
#    tax = 0.13
#print('The '+ province.capitalize() + ' Tax is: ' + str(tax))

# If only one of the conditions will ever occur
# you can use a single if statement with elif
#province = input('Enter the name of your home country: ')
#if province.capitalize() == 'Alberta':
#    tax = 0.05
#elif province.capitalize() == 'Nunavut':
#    tax = 0.05
#elif province.capitalize() == 'Ontario':
#    tax = 0.13
#print('The '+ province.capitalize() + ' Tax is: ' + str(tax))

# When you use elif instead of 
# multiple if statements you can add a default action
#province = input('Enter the name of your home country: ')
#if province.capitalize() == 'Alberta':
#    tax = 0.05
#elif province.capitalize() == 'Nunavut':
#    tax = 0.05
#elif province.capitalize() == 'Ontario':
#    tax = 0.13
#else:
#    tax = 0.15
#print('The '+ province.capitalize() + ' Tax is: ' + str(tax))

# If multiple conditions cause the same 
# action they can be combined into a single condition
#province = input('Enter the name of your home country: ')
#if province.capitalize() == 'Alberta' \
#    or province.capitalize() == 'Nunavut': 
#    tax = 0.05
#elif province.capitalize() == 'Ontario': 
#    tax = 0.13
#else: # 15%
#    tax = 0.15
#print('The '+ province.capitalize() + ' Tax is: ' + str(tax))

# How OR statements are processed
# First Condition | Second Condition | Condition evaluate as
# TRUE | TRUE | TRUE
# TRUE | FALSE | TRUE
# FALSE | TRUE | TRUE
# FALSE | FALSE | FALSE

# If you have a list of possible values to check, 
# you can use the IN operator
#province = input('Enter the name of your home country: ')
#if province.capitalize() in('Alberta',
#                            'Nunavut', 'Yukon'):
#    tax = 0.05
#elif province.capitalize() == 'Ontario': 
#    tax = 0.13
#else: # 15%
#    tax = 0.15
#print('The '+ province.capitalize() + ' Tax is: ' + str(tax))

# If an actions depends on a combination of 
# conditions you can nest if statements
country = input('Enter the name of your home country: ')
if country.capitalize() == 'Canada':
    province = input('Enter the name of your home province: ')
    if province.capitalize() in('Alberta',
                                'Nunavut', 'Yukon'):
        tax = 0.05
    elif province.capitalize() == 'Ontario':
        tax = 0.13
    else: # 15%
        tax = 0.15
else: # 0%
    tax = 0.0
print('The '+ province.capitalize() + ' Tax is: ' + str(tax))