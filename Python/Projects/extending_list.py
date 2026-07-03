class SuperList():
    def __len__(self):
        return 1000

superlist1 = SuperList()

print(len(superlist1))
superlist1.append(5) # 'SuperList' object has no attribute 'append'

# we need to be able to append!