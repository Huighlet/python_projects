# Introducing while loops
# The while loop in action

current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1

prompt = "\nTell me shomething, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
	message = input(prompt)

	if message != 'quit':
		print(message)

# Let's add a flag to the program, this flag
#will monitor whether or not the program should
#continue running:
active = True
while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)

# Using break to Exit a Loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
	city = input(prompt)

	if city == 'quit':
		break
	else:
		print(f"I'd love to go to {city.title()}")

# Using continue in a loop
current_number = 0
while current_number <10:
	current_number += 1
	if current_number % 2 == 0:
		continue

	print(current_number)

# Avoiding infinite loops
x = 1 
while x <= 5:
	print(x)
	x += 1

# Using a shile loop with lists and dictionaries
# Moving items from one list to another
# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candac']
confirmed_users = []

# Verify each user until there are no more unconfirmed users. 
# Move each empty list to hold confirmed users. 
while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print(f"Verifying user: {current_user.title()}")
	confirmed_users.append(current_user)

# Display all confirmed users. 
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

# Removing all instances of specific values from a list 
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cats' in pets:
	pets.remove('cat')

print(pets)

