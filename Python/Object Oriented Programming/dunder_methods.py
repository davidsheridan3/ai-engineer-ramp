class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'John',
            'age': 21,
            'hobby': 'football'
        }

    def __str__(self): # here we actually change the method
        return f'{self.color}' # now lines 10 and 11m print "red"

    def __len__(self):
        return 5

    def __call__(self): # under the hood we actually use this dunder to call functions
        return 'yess??'

    def __getitem__(self, i):
        return self.my_dict[i]

action_figure = Toy('red', 10)
print(action_figure.__str__()) # str dunder method is the same as using the function on the next line
print(str(action_figure))

print(len(action_figure)) # 5
print(action_figure.__len__())

# changed the len dunder to return 5, and changed str dunder to return color

print(action_figure()) # enables us to call it

print(action_figure.__getitem__('hobby')) # football
