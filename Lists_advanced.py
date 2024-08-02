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
numbers = list(range(1, 6))
print(numbers)

#Generate even numbers using range()
even_numbers = list(range(2, 11, 2))
print(even_numbers)

#putting 10 squared numbers into a list
squares = []
for value in range(1, 11):
	square = value**2
	squares.append(square)

print(squares)

#simple statistics with list of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

#List Comprehension
squares = [value**2 for value in range(1, 11)]
print(squares)

#counting to twenty
count = [value for value in range(1, 21)]
print(count)

#WORKING WITH PART OF A LIST#
#Slicing a list
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])

#Looping through a slice
players = ['charles', 'martina', 'micheal', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())

#Copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
 
#To prove that the lists are actually seperate list, I'll modefy each
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods  are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)