# we can use inheritance to ensure that all character types need to be signed in

class User:
    def sign_in(self):
        print('logged in')

class Wizard(User): # to inherit, pass the parent class that we want to inherit from
    pass

class Archer(User):
    pass

wizard1 = Wizard()
print(wizard1.sign_in()) # logged in, we inherited functionality from the User class
