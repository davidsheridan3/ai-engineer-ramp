def test(a):
    '''
    Info: this fucntion tests and prints param a
    '''
    print(a)

test(1) # editor now tells us teh doc string when function is hovered over

help(test) # help() prints the doc string
print(test.__doc__) # does the same thing (but as a method)

# Doc strings allow us to comment inside our functions to provide context for users

