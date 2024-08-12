# A passing test
import unittest 
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""Tests for 'name_function.py'."""

	def test_first_last_name(self):
		"""Do names like 'Janis Joplin' work?"""
		formatted_name = get_formatted_name('janis', 'hasub', 'joplin')
		self.assertEqual(formatted_name, 'Janis Hasub Joplin')

	#Adding New Tests
	def test_first_middle_name(self):
		"""Do names like 'Wolfgang Amadeus Mozart' work?"""
		formatted_name = get_formatted_name(
		'wolfgang', 'mozart', 'amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Mozart Amadeus')

if __name__ == '__main__':
	unittest.main() 