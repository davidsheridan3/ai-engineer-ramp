#Exercise!

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

# Iterate over picture.
    # if 0 -> print ''
    # if 1 -> print '*'


for row in picture:
    for pixel in row:
        if pixel == 0:
            print(" ", end='')
        else:
            print("*", end='')
    print('')

