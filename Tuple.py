#Defining Tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#Looping through all values in a tuple
for dimension in dimensions:
	print(dimension)

#Writing over a tuple
print("Original dimensions")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("Modified dimensions")
for dimension in dimensions:
	print(dimension)