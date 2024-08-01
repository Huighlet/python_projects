#Looping through an entire list
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)

#doing more within a for loop
	print(f"{magician.title()}, that was a great trick")
	print(f"I can't wait to see your next trick, {magician.title()}")

#Doing something after the loop 
print("Thank you, everyone. That was a great magic show!")


#MAKING A NUMERICAL LISTS#
#Using the range() Function
for value in range(1, 5):
	print(value)

#Using range() to Make a list of numbers
numbers = list(range(0, 6))
print(numbers)