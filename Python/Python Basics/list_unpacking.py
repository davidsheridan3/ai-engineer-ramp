a,b,c, *other  = [1,2,3,4,5,6,7,8,9,10]
print(a)
print(b)
print(c)
print(other) # unpacks 1,2,3 from list (just 4-10)


a,b,c, *other, d = ['orange','red','blue','green','purple','black','white']
print(a)
print(b)
print(c)
print(other) # unpacks green, purple, black
print(d) # just prints last item in list