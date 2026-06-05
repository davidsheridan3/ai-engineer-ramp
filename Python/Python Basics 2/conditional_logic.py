is_old = False
is_licenced = True

if is_old:
    print('You are old enough to drive!')
elif is_licenced:
    print('You are licenced! You can drive now') # this runs as is_old = False, and is_licenced = True
else:
    print('You are not old enough to drive!') # else: only runs if all other things fail

print('After conditional block')