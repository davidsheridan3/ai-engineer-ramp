# use case: collecting emails of interested customers
import re
pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
string = 'b@b.com'
string2 = 'ben.com'


a = pattern.search(string)
print(a) # works, yesssss

b = pattern.search(string2)
print(b) # none, doesn't fit the pattern criteria