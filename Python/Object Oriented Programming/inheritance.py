# we can use inheritance to ensure that all character types need to be signed in

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
wizard1.attack() # attacking with power of 100
archer1.attack() # attacking with 50 arrows

# both of these have sign in function at the same time (extracting away part of code that they both share)
# power of inheritance ^^^^


