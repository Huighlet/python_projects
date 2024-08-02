#A simple example
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

#Checking for inequality(string comparison)
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
	print("Hold the anchovies")

#Numerical comparison
answer = 17

if answer != 42:
	print("That is not the correct answer. Please try again!")

#Using multiple check conditions
age_0 = 22
age_1 = 18

if age_0 >= 21 and age_1 >= 21:
	print("False")
else:
	print("True")

#Using (OR) when checking for multiple conditions
age_0 = 22
age_1 = 18

if age_0 >= 21 or age_1 >= 21:
	print("True")


#checking the values in a list 
requested_topping = ['mushrooms', 'onions', 'pineaple']

if 'pepperoni' in requested_topping:
	print("True")
else:
	print("false")

#Checking whether a value is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
	print(f"{user.title()}, you can post a response if you wish.")

#simple if statements
age = 19
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")

#if else statements
age = 17
if age >= 18:
	print("You are old enough to vote")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote")
	print("Please register to vote as soon as you turn 18")

#The if-elif-else chain
age = 12

if age < 4:
	print("Your admission cost is $0")
elif age < 18:
	print("Your admission cost is $25")
else:
	print("Your admission cost is $40")

if age < 4:
	price = 0
elif age < 18:
	price = 25
else:
	price = 40

print(f"Your admission cost is ${price}")


if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
else:
	price = 20

print(f"Your admission cost is ${price}")

#Testing multiple conditions
requested_topping = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_topping:
	print("Adding mushrooms")
if 'pepperoni' in requested_topping:
	print("Adding pepperoni")
if 'extra cheese' in requested_topping:
	print("Adding extra cheese")

print("\nFinished making your pizza")

#using for to test multiple conditions
for requested_toppings in requested_topping:
	print(f"Adding {requested_toppings.title()}")

print("\nFinished making your pizza")

#combining if and for 
for requested_toppings in requested_topping:
	if requested_toppings == 'mushrooms':
		print("Sorry, we are out of mushrooms right now")
	else:
		print(f"Adding {requested_topping}")

print("\nFinished making your pizza")

#checking that a list is not empty 
requested_topping = []

if requested_topping:
	for requested_toppings in requested_topping:
		print(f"Adding {requested_topping}")
		print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza")

#Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green pepper', 
						'pepperoni', 'pineaple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")