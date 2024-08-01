#this is how lists are supposed to be used on python

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#accessing Elements in a list

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[0].title())
#this code returns second and fourth bicycles in the list:
print(bicycles[1])
print(bicycles[3])
#this code returns the last item in a list (-1)
print(bicycles[-1])

#using individual values in a list 
message = f"My first bicycle was a {bicycles[0].title()}"
print(f"{message}, \n")

#modifying Elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

#adding elements to a list (end of the list)
motorcycles.append('ducati')
print(motorcycles)

#adding elements to an empty list
goodmotocycles = []

goodmotocycles.append('honda')
goodmotocycles.append('yamaha')
goodmotocycles.append('suzuki')
print(goodmotocycles)

#adding anything to a particular position of the list usning insert()
motorcycles.insert(0, 'ducati')
print(motorcycles)

#removing elements from a list (using the del statement)
del motorcycles[0]
print(motorcycles)

#removing the second item in the list (using the del statement)
del motorcycles[1]
print(motorcycles)

#Removing an item using the pop() method
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

#forming a sentence with the pop() element
print(f"The last motorcycle I owned was a {popped_motorcycles.title()}.")

#popping items from any position in a list 
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")


#Removing an Item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()}, is too expensive for me.")

#ORGANIZING A LIST#
#Sorting a list permanently with the sort() Method
cars = ['bmv', 'audo', 'toyota', 'subaru']
cars.sort()
print()

#sorting a list in reverse alphabetically by passing the (reverse=True) method
cars.sort(reverse=True)
print(cars)

#sorting a list temporarily with the sorted() function.
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#printing a list in reverse order
cars.reverse()
print(cars)

#Finding the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)
print(len(cars))