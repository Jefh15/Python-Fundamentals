# Demo Conditional handling

#price = input('How much did you pay?: ')
#convert to a float number
#price = float(price)
#if price >= 1.00:
#    tax = .07
#else:
#    tax = 0
#print('Tax rate is: ' + str(tax))


country = input('Enter the name of your home country: ')
if country.capitalize() == 'Canada':
    print('So you must like hockey!')
else:
    print('You are not from Canada')
