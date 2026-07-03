class User:
    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def check_arrows(self):
        print(f'{self.num_arrows} arrows remaining.')

    def run(self):
        print('Running really fast!')

class Hybrid(Wizard,Archer): # we want Hybrid to be able to access all methods
    pass

hybrid1 = Hybrid('Hybry',100)
print(hybrid1.run()) # Running really fast!
print(hybrid1.check_arrows()) # 'Hybrid' object has no attribute 'num_arrows'

# this error is happening because we inherited from Wizard first, then Archer, and Wizard accepts: name, power

