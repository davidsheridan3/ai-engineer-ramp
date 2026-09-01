import re

pattern = re.compile(r"([a-zA-Z]).([a])") # to search for any letter, followed by anything, followed by a
string = 'search for his wallet'

a = pattern.search(string)
print(a.group()) # sea
print(a.group(1)) # s
print(a.group(2)) # a