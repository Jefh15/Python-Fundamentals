
######################################################################
# DESCRIPTION FILE
# Calling an API
# What is a web service ?
# When a developer want to share the 
# functionality of a function but not the
# actual code in the program, they can place the 
# function on a web server
# A programmer with the address of that function
# on the web server and the required permissions 
# can call the function
# This is called a web service
# Pythoncode -> ...... http://contoso 
# ( analyze(),
# ocr(), recognizeText() 
# )

# https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/quickstarts-sdk/image-analysis-client-library-40?tabs=visual-studio%2Clinux&pivots=programming-language-python

# https://free-apis.github.io/#/categories/Animals
# https://random.dog/woof.json
# https://developers.thecatapi.com/view-account/ylX4blBYT9FaoVd6OhvR?report=bOoHBz-8t
# https://api.thecatapi.com/v1/images/search?limit=10

# What is an API
# You can't call a function unless you know the 
# function name and the required parameters

# When you create a web service you create an Application
# Programming Interface (API)

# The API defines the function and parameters so others 
# know how call your function.

# Example: 
# analyze(visualfeatures, details, language)

# Keys allow me to track wich users have 
# permission to use my web service

# A developer signs up on my web site, or buys a license 
# for my software and is provided a unique key

# When the developer calls my web service they 
# provide their unique key and I am able to verify 
# the key has been approved fr calls to my web service 

# There is a standard for sending messages across the web
# Hypertext Transfer PRotocol (HTTP) is a standard protocol 
# for sending messages across the web
# GET -> Pass values in query string only
# GET -> Special characters musb be "escaped"
# GET -> Limited ammount of data

# POST -> Pass values in query string and body
# POST -> No need to escape special characters if passed in body
# POST -> Can pass large amounts of data, 
#         including images, in body

# The requests library
# simplifies HTTP calls from Python code
# requests.post(address, http_headers, 
#               function_parameters, message_body)

# http_headers ---> content-ty, API key
# function_parameters ---> too much
# message_body --> "url": "IMAGE URL"


#####################################################################
#IMPORTS


#####################################################################
#FUNCTIONS

##################################################################
# MAIN CODE
