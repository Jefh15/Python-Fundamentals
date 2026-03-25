# Stings can be store in variables
first_name = 'Jesus'
print(first_name)

# Conbine strings with +
last_name = 'Fonseca'
print(first_name + ' ' + last_name)
print('Hello, ' + first_name + ' ' + last_name)

# You can use functions to modify strings
sentence = 'The dog is named Raider'
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('a'))

# Functions help us format strings we save to 
# files and databases, or display to users
first_name = input('What is your name: ')
last_name = input('What is your last name: ')
print('Hello ' + 
      first_name.capitalize() + 
      ' '+ last_name.capitalize()
    )
