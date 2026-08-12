# Error Handling

# def sum(num1, num2):
#     return num1 + num2
#
# print(sum('1', '2')) # output = 12, just adds strings together

def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f'Please enter a number {err}') # err useful to give meaningful errors to users

print(sum(1, '2')) # Something went wrong, but far too vague

