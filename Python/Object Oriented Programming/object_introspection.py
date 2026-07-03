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

print(dir(wizard1)) # gives all of methods and attributes that wizard instance has