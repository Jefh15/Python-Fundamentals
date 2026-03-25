
######################################################################
# DESCRIPTION FILE
# https://sample.json-format.com/
# Javascript Object Notation (JSON)
# Many web services return data as JSON
# JSON is a standard data format that can be 
# intimidating at fisrt glance

# results
# {"colors": {....}, "metadata":{"width": 220,"height": 220,"format": "Jpeg",}}

# Using a linting tool to format JSON makes it easier to read

# JSON contains key pairs like Dictionary collection 

# "Key": "value"
# "requestId": "33as3d3a-asd4-asd4-asds-sssd5886"

# JSON can contains subkeys and subvalues
# "color": {
# "dominantColor": "White",
# "dominantColors": ["White"],
# "accentColor": "589554",
# "isBWImg": "false",
# }

# JSON can contains list of values
# {
#   "tags": ["bear","animal","and so one..."]
# }


# How to create JSON in my code
# usualmente usamos diccionarios
# CREATE A DICTIONARY OBJECT
# person_dict = {'first': 'Jesus', 'last': 'Fonseca'}
# Add additional key pairs as need to dictionary
# person_dict['City']='San Jose'

# convert dictionary to JSON Object
# json.dumps()
# person_dict = json.dumps(person_dict)
# print(person_json)
# {'first': 'Jesus', 'last': 'Fonseca','City': 'San Jose'}


# Dictiory in a Dictionary
# Dictionary = {}
# Nest dictionaries to create JSON in format
# {"Key": {"Subkey0": "subvalue0","Subkey1": "subvalue1",...}}
# person_dict = {'first': 'Jesus', 'last': 'Fonseca','City': 'San Jose'}

# CREATE STAFF DICTIONARY WHICH 
# ASSIGNS A PERSON TO A ROLE
# staff_dict = {}
# staff_dict['Program Manager']=person_dict

# Convert dictionary to JSON object
# staff_json = json.dumps(staff_dict)

# Print JSON Object
# print(staff_json)
# {
#   "Program Manager":  {
#                           'first': 'Jesus', 'last': 'Fonseca','City': 'San Jose'
#                       }
# }


# List in a Dictionary
# LISTs = []
# Add lists to the dictionary to create
# JSON in the format
# {"Key": ['listvalue0','listvalue1','....']}


# person_dict = {'first': 'Jesus', 'last': 'Fonseca'}

# Initialize the languages_list
# languages_list = []

# Create a list object of programming languages
# languages_list['CSharp', 'Python', 'Java', 'Javascript']

# Add list languages_list to dictionary person_dict
# person_dict['languages']=languages_list

# Convert dictionary to JSON object
# person_json = json.dumps(person_dict)

# Print JSON Object
# print(person_json)
# {
#   "first": "Jesus", 
#   "last": "Fonseca",
#   "languages_list": [
#                       "CSharp", 
#                       "Python",
#                       "Java",
#                       "Javascript"
#                     ]
# }


# When creating and reading
# Use print statements to help you debug
# Use a JSON liting too to make the JSON easier 
#   to read
# Have a print out of the full JSON 
#   so you can figure out the 
#   structure when reading specific elements 

#####################################################################
#IMPORTS

#####################################################################
#FUNCTIONS

####################################################################
# MAIN CODE

# To retrieve the value from a "key":"value"
# request the key name
# results
# "requestId": "33as3d3a-asd4-asd4-asds-sssd5886"
# print(results['requestId'])
# it will return the value if we pass the key
# 33as3d3a-asd4-asd4-asds-sssd5886


# Think this like folder and subfolder
# what can i do if need to return a value
# that i will be in those subkies
# so i have the color key and i want to know
# the dominantColor value
# "color": {
# "dominantColor": "White",
# "dominantColors": ["White"],
# "accentColor": "589554",
# "isBWImg": "false",
# }

# i will print the key called dominantColor 
# # print(results['color']['dominantColor'])
# and it will return the value 
# White


# Now if we have a list
# "description":
# {
#   "tags": [
#               "bear",
#               "animal",
#               "outdoor",
#               "future",
#               "indooor",
#               "black",
#               "red",
#               "and so one..."
#           ],
#   "captions": [
#                   {"text": "acbdef...", 
#                   "confidence"}
#               ]
# }

# so i want the first value of a list
# print(results['description']['tags'][0])
# and it will return
# bear

# and if i want all values of a list of object
# for item in results['description']['tags]:
# print(item)
#               "bear",
#               "animal",
#               "outdoor",
#               "future",
#               "indooor",
#               "black",
#               "red",
#               "and so one..."