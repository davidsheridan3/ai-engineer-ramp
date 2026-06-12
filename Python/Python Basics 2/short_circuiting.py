# Short Circuiting
is_friend = True
is_user = True

if is_friend or is_user: # sort circuiting: interpreter sees that is_friend = True, so just jumps to the next line (print)
    print("best friends forever!")