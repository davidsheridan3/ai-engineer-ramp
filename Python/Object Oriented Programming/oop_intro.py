# OOP
class BigObject: # class
    pass

obj1 = BigObject() # instanciate
obj2 = BigObject()
obj3 = BigObject()

# now I have 3 different objects I can use based on blueprint defined earlier

# Creating our own objects:

class PlayerCharacter:
    # Class Object Attribute
    membership = True # static, this is going to be true and exist for all objects
    def __init__(self, name = "Anonymous", age= 0): # self refers to PlayerCharacter, with default args too, for if user leaves out name or age
        if (age > 18):
            self.name = name # self refers to player
            self.age = age

    def run(self):
        print('run')

player1 = PlayerCharacter('David',19) # object 1
player2 = PlayerCharacter('Marcus',22) # object 2
print(player1.age) # <__main__.PlayerCharacter object at 0x100a5ce80>
print(player2.name) # Marcus

# self allows us to have a reference to something that hasn't between created yet
# self allows us to write code only once, and make it dynamic, and change based on what we give it