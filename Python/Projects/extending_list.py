class SuperList(list):
    def __len__(self):
        return 1000

superlist1 = SuperList()

print(len(superlist1))
superlist1.append(100) # 'SuperList' object has no attribute 'append'
print(superlist1[0])

print(issubclass(SuperList, list)) # True, SuperList is a subclass of list

