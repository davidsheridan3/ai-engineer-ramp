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
    def __init__(self, name, power,  num_arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, num_arrows)

hybrid1 = Hybrid('Hybry',100, 500)
print(hybrid1.run()) # Running really fast!
print(hybrid1.check_arrows()) # 500 arrows remaining.


