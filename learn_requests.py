"""Exercises to learn requests"""

import requests, json

from requests.exceptions import Timeout, ConnectionError as RqConnectionError
from requests.exceptions import HTTPError

# ==================================================================
# Exercise 1: Get requests on JSONPlaceholder posts, users & todos
# ==================================================================

response_posts = requests.get('https://jsonplaceholder.typicode.com/posts') # Get all the posts
response_users = requests.get('https://jsonplaceholder.typicode.com/users') # Get all the users
response_todos = requests.get('https://jsonplaceholder.typicode.com/todos')

print(f"Status code: {response_posts.status_code}\n") # Display the code status
print(f"Header:\n{json.dumps(dict(response_posts.headers), indent=4)}\n") # Display the request header
print(f"First post:\n{json.dumps(response_posts.json()[0], indent=4)}\n") # Get the first post

print(f"Status code: {response_users.status_code}\n") # Display the code status
print(f"Header:\n{json.dumps(dict(response_users.headers), indent=4)}\n") # Display the request header
print(f"First user:\n{json.dumps(response_users.json()[0], indent=4)}\n") # Get the first user

print(f"Status code: {response_todos.status_code}\n") # Display the code status
print(f"Header:\n{json.dumps(dict(response_todos.headers), indent=4)}\n") # Display the request header
print(f"First todo:\n{json.dumps(response_todos.json()[0], indent=4)}") # Get the first todo


# ==================================================
# Exercise 2: Post request on JSONPlaceholder posts
# ==================================================

# Define the post to post on JSONPlaceholder
post = {
    "userId": 199681,
    "id": 199681,
    "title": "requests learning",
    "body": "A simple test to learn how to use requests librairy"
}

# Post request to post a new post
request_post = requests.post('https://jsonplaceholder.typicode.com/posts', json=post)

print(f"\nPost request status: {request_post.status_code}") # Check the status code
print(f"Response body:\n{json.dumps(request_post.json(), indent=4)}\n") # Display the response body


# =============================================================
# Exercise 3: Handle timeout and error code status (4xx, 5xx)
# =============================================================

# Handle timeout
try:
    # Simulate a timeout
    timeout_response = requests.get('https://jsonplaceholder.typicode.com/posts', timeout=0.01)
    #timeout_response = requests.get('https://httpbin.org/delay/5', timeout=1)

except Timeout as e: # Catching the Timeout error
    print(f"Error: {e}")

except RqConnectionError as e: # Catching request connection error
    print(f"Error request: {e}")

except ConnectionError as e: # Catching python connection error
    print(f"Error python: {e}")

else: # Request status code if no timeout is catching 
    print(f"Request status: {timeout_response.status_code}")


# Handle error code status (4xx, 5xx)
try:
    status_response = requests.get('https://jsonplaceholder.typicode.com/posts/999999') # This URL doesn't exist
    status_response.raise_for_status() # Raise an error if the code is upper than 399

except HTTPError as e:
    print(f"Error: {e}") # Display the error

else:
    print(f"Request success: {status_response.status_code}")


# =================================================
# Exercise 4: Automatic pagination with generator
# =================================================

# Generator pagination
def pagination():
    """Function to work through the pages of posts."""
    page = 1 # Initialize pagination
    while True:
        # Make request untill the end of the posts
        response = requests.get(
            f'https://jsonplaceholder.typicode.com/posts/',
            params={"_page": page, "_per_page": 10}
            )
        if not response.json(): # Check if there are no results
            break
        else:
            yield response.text
            page += 1

# Display post
for index, p in enumerate(pagination()):
    print("{:=^200}".format(""))
    print("{: ^200}".format(f"Page {index+1}"))
    print("{:=^200}".format(""))

    print(f"\n{p}\n")




