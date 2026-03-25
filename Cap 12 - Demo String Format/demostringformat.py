# Custom string formatting
first_name = 'Jesus'
last_name = 'Fonseca'
output = 'Hello 1, ' + first_name + ' ' + last_name
print(output)

# Without specify
output = 'Hello 2, {} {}'.format(first_name, last_name)
print(output)

# With specify the parameter number
output = 'Hello 3, {1} {0}'.format(first_name, last_name)
print(output)

# Only available in Python 3
output = f'Hello 4, {first_name} {last_name}'
print(output)

