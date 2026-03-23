"""Exercises to learn requests"""

import requests, json

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
print(f"Response body:\n{json.dumps(request_post.json(), indent=4)}") # Display the response body
