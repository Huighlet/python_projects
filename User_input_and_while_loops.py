# How the input() functions works
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# writing Clear Prompts
name = input("Please enter your name: ")
print(f"\nHello, {name}!")

prompt = "If you tell us who you are, we can personlize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)

#Accepting integer inputs
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
	print("\nYou're tall enough to ride!")
else: 
	print("\nYou'll be able to ride when you're when you're a little older")

# The modulo Operator
number = input("Enter a number, and i'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
	print(f"\nThe number {number} is even.")
else:
	print(f"\nThe number {number} is odd. ")

#Rental Car: Write a program that asks the user what kind of rental car they
#would like. Print a message about that car, such as “Let me see if I can find you
#a Subaru.”
car_rental = input("What kind of rental car would you like? ")
print("Let me see if i can find you a Subaru")

#Restaurant Seating: Write a program that asks the user how many people
#are in their dinner group. If the answer is more than eight, print a message say-
#ing they’ll have to wait for a table. Otherwise, report that their table is ready
restaurantseating = input("How many are you people at the dinner table: ")
restaurantseating = int(restaurantseating)

if restaurantseating >= 8:
	print("\nYou'll have to wait for the table")
else:
	print("\nReport your table is ready.")

#Multiples of Ten: Ask the user for a number, and then report whether the
#number is a multiple of 10 or not.
number = input("\nEnter a number which is a multiple of 10: ")
number = int(number)

if number % 10 == 0:
	print("\nThis number is a multiple of 10")
else:
	print("\nThis number is not a multiple of 10")