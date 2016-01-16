def yield_shii():
    for item in xrange(1, 51):
        yield (item, item ** 2)


for digit, digit_square in yield_shii():
    print "The square of {:03d} is {:03d}".format(digit, digit_square)
