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

# Reorganize the code by writing two functions.
def print_models(unprinted_designs, completed_models):
	"""
	Simulate printing each design, until none are left.
	Move each design to completed_models after printing.
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"Printing model: {current_design}")
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""Show all the models that were printed. """
	print("\nThe following models have been printed: ")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#Passing an Arbitrary Number of Arguments
def make_pizza(*toppings):
	"""Print the list of toppings that have been requested"""
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#Mixing positional and arbitrary arguments
def make_pizza(size, *toppings):
	"""Summarize the pizza we are about to make. """
	print(f"\nMaking a {size}-inch pizza with the following toppings.")
	for topping in toppings:
		print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#Using Arbitrary Keyword arguments
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('albert', 'einstein',
								location = 'priceton',
								field = 'physics')

print(user_profile)

