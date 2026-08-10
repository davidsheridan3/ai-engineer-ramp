from functools import reduce
from string import capwords

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
my_pets_upper = [word.capitalize() for word in my_pets]
print(my_pets_upper)


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

sorted_numbers = sorted(my_numbers)

zipped = (list(zip(my_strings, sorted_numbers)))
print(zipped)



#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def over_50(scores):
    return scores > 50

print(list(filter(over_50, scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
scores = [73, 20, 65, 19, 76, 100, 88]
my_numbers = [5, 4, 3, 2, 1]

combined = scores + my_numbers

def accumulator(total, num):
    return total + num

print(reduce(accumulator, combined))