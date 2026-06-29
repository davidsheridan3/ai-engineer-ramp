class User:
    def sign_in(self):
        print('logged in')

class Wizard(User): # to inherit, pass the parent class that we want to inherit from
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with {self.num_arrows} arrows')

wizard1 = Wizard('David', 100)
archer1 = Archer('John', 50)

# polymorphism here, depending on which attribute we call, the attack method acts differently:

wizard1.attack() # attacking with power of 100
archer1.attack() # attacking with 50 arrows

# to display this within the same function:
def player_attack(character):
    character.attack()

player_attack(wizard1) # attacking with power of 100
player_attack(archer1) # attacking with 50 arrows

# the same function gives us a different output, because oif the object we pass into it = POLYMORPHISM!!!
