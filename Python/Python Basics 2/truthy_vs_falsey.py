# Truthy vs falsey

is_old = "Helloooooo" # True
is_licenced = 5 # True

if is_old and is_licenced:
    print('You are old enough to drive, and you have a licence!')
else:
    print('You need to be old enough and have a licence..... not today buddy!') # else: only runs if all other things fail

print('After conditional block')

print(bool(is_old)) # True, this is a truthy value!
print(bool(is_licenced)) # True, this is a truthy value!

# So, what is a falsey value?
is_red = ''
is_blue = 0
is_green = '0'

print(bool(is_red)) # False, this is a falsey value!
print(bool(is_blue)) # False, this is a falsey value!
print(bool(is_green)) # True, this is a truthy value!