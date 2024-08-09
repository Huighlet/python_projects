# Creating and using a class 
# Creating the dog class
class Dog:
	"""A simple attempt to model a dog. """
	def __init__(self, name, age):
		"""initialize name and age atributes. """
		self.name = name
		self.age = age

	def sit(self):
		"""simulate a dog sittiong in response to a command. """
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Calling methods
my_dog.sit()
my_dog.roll_over()

# Creating multiple instances
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} your old.")
your_dog.sit()

# Working with classes and instances
# The car class
"""A class that can be used to represent a car. """
class Car:
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		"""Setting a default value for an attribute"""
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neately formatted description name."""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing the car's mileage. """
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odemeter(self, mileage):
		"""
		Set the odometer reading to the given value.
		Reject the change if it attempts to roll the odometer back.	
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		"""Add the given amount to the odemeter reading. """
		self.odometer_reading += miles

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odemeter(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
# Modifying attribut value
# Mddifying an attribute's value directly
my_new_car.odometer_reading = -1
# Modifying an attribute value through a method
my_new_car.update_odemeter(-1)
my_new_car.read_odometer()

# intances as attributes
class Battery:
	"""A simple attempt to model battery fo an electric car. """

	def __init__(self, battery_size=75):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size}-KWh battery")

	def get_range(self):
		"""Print a statement about the range this battery provides. """
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315

		print(f"This car can go about {range} miles on a full charge.")

# Inheritance
class ElectricCar(Car):
	"""Represent aspect of a car, specific to electric vehicle. """

	def __init__(self, make, model, year):
		"""
		Initialize attributes of the parent class. 
		Then initialize attributes specific to an electric car. 
		"""
		super().__init__(make,model,year)
		self.battery_size = 75
		self.battery = Battery()

	def describe_battery(self):
		"""Print a statement describing the battery size. """
		print(f"This car has a {self.battery_size}-KWh battery.")

	# Overriding methods from the parent class
	def fill_gas_tank(self):
		"""Electric cars don't have gas tanks."""
		print("This car doesn't need a gas tank!")

	

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
