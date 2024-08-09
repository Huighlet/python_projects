"""A set of classes that can be used to represent electric cars."""
from Classes import Car

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
