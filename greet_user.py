# now let's greet users with the name that has been stored
import json

filename = 'username.json'

with open(filename) as f:
	username = json.load(f)
	print(f"Welcome back, {username}")