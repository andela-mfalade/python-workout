import doctest

def squares(n):
	"""Squares n
	
	>>> test_method(9)
	81

	>>> test_method(0)
	0

	>>> test_method(3)
	9
	"""
	
	return n ** 2


if __name__ == "__main__":
	doctest.squares()
