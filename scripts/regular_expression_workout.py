import re


test_string = "This is the key to the kingdom. Guess what..There are more keys"
match_ = re.match(r'(.*) are (.*?) .*', test_string, re.M | re.I)

if match_:
    print match_.groups()
else:
    print "No match was found for this pattern"
