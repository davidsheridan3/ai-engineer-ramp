print(True == 1) # True
print('' == 1) # False
print([] == 1) # False
print(10 == 10.0) # True
print([] == []) # True

# '==' doesn't check for equality of type, it checks for equality of value

# 'is' then:
print(True is 1) # False
print('' is 1) # False
print([] is 1) # False
print(10 is 10.0) # False
print([] is []) # False

# 'is' is stricter, you're checking for the exact thing that you're looking for, not it's value
a = [1,2,3]
b = [1,2,3]
print(a == b) # True
print(a is b) # False
print(a is a) # True