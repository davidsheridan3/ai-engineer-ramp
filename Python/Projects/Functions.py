# Create a function to return the highest even number

def highest_even(*numbers):
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return max(evens)

print(highest_even(1,2,3,4,5,6,7,9,11)) # 6
