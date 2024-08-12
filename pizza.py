# Storing your functions in modules
def make_pizza(size, *toppings):
	"""Summarize the pizza we are about to make."""
	print(f"\nMaking a {size}-inch pizza with following toppings:")
	for topping in toppings:
		print(f"- {topping}")