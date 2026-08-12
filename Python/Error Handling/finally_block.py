# Error Handling

while True:
    try:
        age = int(input('Enter your age: '))
        10/age
    except ValueError:
        print('Please enter a number!')
    except ZeroDivisionError:
        print('Please enter a number greater than 0!')
    else:
        print('Thank you for your time!')
        break
    # finally block gets ran at the end of each output, regardless
    finally:
        print('That is all for now!')