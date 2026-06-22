# Scope - what variables do I have access to?

total = 100 # global scope

def sum_func():
    total2 = 200

if True:
    x = 5000

print(total) # 100, as it's part of global scope
print(total2) # error, as it's local scope
print(x) # 5000, although indented, part of global scope
