# numeric variables
pi = 3.14159
print(pi)

# You can do math with numbers
# Symbol | Operation
# + | Addition
# - | Subtraction
# * | Multiplication
# / | Vivision
# ** | Exponent
first_num = 6
second_num = 2
print(first_num + second_num)
print(first_num - second_num)
print(first_num * second_num)
print(first_num / second_num)
print(first_num ** second_num)

# If you combine strings with numbers, Python get confused
#days_in_feb = 2
#print(days_in_feb + ' days in February')
# Traceback (most recent call last):
# File "/home/crekoj/Documentos/Jesus/Desarrollo/Learn Python/Cap 13 - Numeric Data Types/numericdatatypes.py", line 22, in <module>
#    print(days_in_feb + ' days in February')
#          ~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~
#TypeError: unsupported operand type(s) for +: 'int' and 'str'

# When displaying a string that contains
# numbers you most convert the numbers into strings
days_in_feb = 28
print(str(days_in_feb) + ' days in February')

# Numbers can be stored as strings
# Numbers stored as strings are treated as strings
first_num = '5'
second_num = '6'
print(first_num + second_num)
print(int(first_num) + int(second_num))

# The input function always returns strings
# Numbers stored as strings must be converted to
# numeric values before doing math
first_num = input('Enter first number: ')
second_num = input('Enter second number: ')
print(first_num + second_num)
print(int(first_num) + int(second_num))
print(float(first_num) + float(second_num))

# Numeric values are used for math operations
# and to specify individual rows in lists and arrays
# index | module name
# 0 | Data Science Concepts
# 1 | Preparing your data
# 2 | Selecting features
# 3 | Splitting your data
# 4 | Selecting an algorithm
# 5 | Training your model
price = 5
federal_tax = 6
price_with_tax = price + price * federal_tax
#module(current_module)