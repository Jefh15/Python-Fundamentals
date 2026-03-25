# Custom string formatting
first_name = 'Jesus'
last_name = 'Fonseca'
output = 'Hello ' + first_name + ' ' + last_name

# Without specify
output = 'Hello, {} {}'.format(first_name, last_name)
print(output)

# With specify the parameter number
output = 'Hello, {0} {1}'.format(first_name, last_name)
print(output)

# Only available in Python 3
output = f'Hello, {first_name} {last_name}'
print(output)

