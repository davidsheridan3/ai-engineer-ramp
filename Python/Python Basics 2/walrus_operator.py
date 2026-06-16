a = 'helllllooooooooo'

if (n := len(a)) > 10: # assigning len(a) to variable n
    print(f"Too long, {n} characters")

# Allows us to assign values to variables as part of a larger expression

while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]

print(a) # h