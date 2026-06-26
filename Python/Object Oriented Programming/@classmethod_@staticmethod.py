# OOP
class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f'{self.name} is {self.age} years old')

    @classmethod # this is a method on the actual class, we can use it without instantiating a class
    def adding_things(cls, num1, num2):
        return num1 + num2

    @staticmethod # we use static when we don't care about the class state (attributes)
    def adding_things2(num1, num2):
        return num1 + num2

player1 = PlayerCharacter('David',19)
player2 = PlayerCharacter('Marcus',22)

# print(player1.adding_things(5,7))
print(PlayerCharacter.adding_things(12,23)) # 35
