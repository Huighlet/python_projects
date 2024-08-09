# Reading from a file
# Reading an entire file

with open('pi_digits.txt') as file_object:
	contents = file_object.read()
print(contents)

# Rading line by line

filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object: 
		print(line)
		"""
		removing newline characters at the end
		of each line in the text file. 
		"""
		print(line.rstrip())

# Making a list of lines from a file

	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())

# Working with a file's contents

pi_string = ''
for line in lines:
	pi_string += line.rstrip()

	print(pi_string)
	print(len(pi_string))