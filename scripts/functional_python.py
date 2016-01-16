# Using map on lists
test_list = range(1, 21)
result = map(lambda x: x ** x, test_list)
print result


# Using fiiter
def is_odd(x):
    return x % 2 == 0

even_numbers = filter(lambda x: x % 2 == 0, result)
odd_numbers = filter(lambda x: x % 2 != 0, result)
print even_numbers
print odd_numbers
