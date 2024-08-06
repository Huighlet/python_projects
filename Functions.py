# Defining a function
def greet_user():
	"""Display a simple greeting."""
	print("Hello!")

greet_user()

# passing information to a function
def greet_user(username):
	"""Display a simple greeting."""
	print(f"Hello, {username.title()}")

greet_user('jesse')

# Passing Argument
# Positional Argument

def describe_pet(animal_type, pet_name):
	"""Display information about a pet"""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
"""Multiple Function Calls"""
describe_pet('dog', 'willie')
"""Order Matters in positional Arguments"""
describe_pet('harry', 'hamster')

# Keyword arguments
describe_pet(animal_type='hamster', pet_name='harry')

# Default Value
def describe_pet(pet_name, animal_type='dog'):
	"""Display information about per."""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()} \n")

describe_pet(pet_name='willie')

#Returning a simple value
def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted"""
	full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Making an Argument Optional
def get_formatted_name(first_name, last_name, middle_name=''):
	"""Return a full name, neatly formatted."""
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# Returning a Dictionary
def build_person(first_name, last_name, age=None):
	"""Return a dictionary of information about a person."""
	person = {'first' : first_name, 'last' : last_name}
	if age:
		person['age'] = age
	return person

musician= build_person('jimi', 'hendrix', age=27)
print(musician)

# Using a function with a while loop
def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted. """
	full_name = f"{first_name} {last_name}"
	return full_name.title()

while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")

	f_name = input("First name: ")
	if f_name == 'q':
		break

	l_name = input("Last name: ")
	if l_name == 'q':
		break

	formatted_name = get_formatted_name(f_name, l_name)
	print(f"\nHello, {formatted_name}!")

# Passing a List
def greet_users(names):
	"""Print a simple greeting to each user in the list."""
	for name in names:
		msg = f"Hello, {name.title()}"
		print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Modifying a list in a function
# Start with some designs that need to be printed. 
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left. 
# Move each design to complete_models after printing. 
while unprinted_designs:
	current_design = unprinted_designs.pop()
	print(f"Printing model: {current_design}")
	completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
	print(completed_model)