# Read the list back into memory using json.load()
import json

filename = 'numbers.json'
with open(filename) as f:
	numbers = json.load(f)

print(numbers)