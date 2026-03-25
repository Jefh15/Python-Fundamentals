
######################################################################
# DESCRIPTION FILE
# Calling an API code
# https://www.google.com/search?q=python+rest+api+call+example&client=ubuntu-sn&hs=Wav&sca_esv=44d106614816f4f2&channel=fs&sxsrf=ANbL-n6qy_BUglTx7AlmLIrPTeHYBxyPWw%3A1773203659348&ei=y_CwafD8FN7OwbkPlbTu-AU&biw=742&bih=747&oq=python+api+request&gs_lp=Egxnd3Mtd2l6LXNlcnAiEnB5dGhvbiBhcGkgcmVxdWVzdCoCCAAyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyDRAAGIAEGLADGEMYigUyFxAuGLADGLgGGNgCGMgDGNoGGNwG2AEBMhcQLhiwAxi4BhjYAhjIAxjaBhjcBtgBATIXEC4YsAMYuAYY2AIYyAMY2gYY3AbYAQFIvxRQAFgAcAF4AZABAJgBAKABAKoBALgBA8gBAJgCAaACDJgDAIgGAZAGDLoGBAgBGBmSBwExoAcAsgcAuAcAwgcDMy0xyAcJgAgA&sclient=gws-wiz-serp

#####################################################################
#IMPORTS

#####################################################################
#FUNCTIONS

##################################################################
# MAIN CODE

#GET
import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"

# Send the GET request
response = requests.get(api_url)

# Check the status code (200 means success)
if response.status_code == 200:
    # Parse the JSON response into a Python dictionary/list
    data = response.json()
    print("Success! Data received:")
    print(data)
    print(f"Title: {data['title']}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

########################
# POST
import requests
import json

api_url = "https://jsonplaceholder.typicode.com/posts"
# The data payload to send, as a Python dictionary
payload = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Send the POST request. The 'json' argument automatically handles JSON serialization
response = requests.post(api_url, json=payload)

# Check the status code (201 means created)
if response.status_code == 201:
    new_post = response.json()
    print("Success! New post created:")
    print(new_post)
else:
    print(f"Failed to create post. Status code: {response.status_code}")

########################
# PUT
import requests

api_url = "https://typicode.com"
update_payload = {
    'title': 'updated title',
    'body': 'updated body',
    'userId': 1
}

# Send the PUT request
response = requests.put(api_url, json=update_payload)

if response.status_code == 200:
    updated_data = response.json()
    print("Success! Resource updated:")
    print(updated_data)
else:
    print(f"Failed to update resource. Status code: {response.status_code}")


########################
# DELETE
import requests

api_url = "https://typicode.com"

# Send the DELETE request
response = requests.delete(api_url)

# Check the status code (200, 204 often mean success)
if response.status_code in [200, 204]:
    print("Success! Resource deleted.")
else:
    print(f"Failed to delete resource. Status code: {response.status_code}")

