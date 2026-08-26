import re

pattern = re.compile('this')
string = 'search inside of this text please this that!'

# a = re.search('this', string)
a = pattern.search(string) # we can use the pattern variable to simplify this search for strings
print(a) # <re.Match object; span=(17, 21), match='this'>

b = pattern.findall(string) # and we can re-use the pattern variable, how efficient!
print(b) # ['this', 'this']

c = pattern.fullmatch(string)
print(c) # none, string being searched for has to fully match string be compared to

d = pattern.match(string)
print(d) # none, matches 0 or more characters at beginning of string 

# print(a) # output = match object: <re.Match object; span=(17, 21), match='this'>
# print(a.span()) # prints where the strings occurs, as a tuple: (17, 21)
# print(a.start()) # 17
# print(a.end()) # 21