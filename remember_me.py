# Saving and reading user-generated Data
import json

"""
username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f:
	json.dump(username, f)
	print(f"We'll remember you when you come back, {username}")
"""
"""
# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it. 
filename = 'username.json'
try:
	with open(filename) as f:
		username = json.load(f)
except FileNotFoundError:
	username = input("What is your name? ")
	with open(filename, 'w') as f:
		json.dump(username,f)
		print(f"We'll remember you when you come back, {username}!")
else:
	print(f"Welcome back, {username}!")
"""
# Refactoring
def get_stored_username():
	"""Get stored username if availble."""
	filename = 'username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None 
	else:
		return username


def greet_user():
	"""Greet ther user by name."""
	username = get_stored_username()
	if username:
		print(f"Welcome back, {username}!")
	else:
		username = input("What is your name? ")
		filename = 'username.json'
		with open(filename, 'w') as f:
			json.dump(username, f)
			print(f"We'll remember you when you come back, {username}!")
greet_user()