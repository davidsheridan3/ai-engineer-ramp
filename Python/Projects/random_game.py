from random import randint

# generate a number 1 - 10
answer = randint(1, 10)

# input from user?

# check that input is a number 1 - 10
while True:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        if  0 < guess < 11:
            if guess == answer:
                print("Correct!")
                break
        else:
            print("Hey, I said 1 - 10!!!")
    except ValueError:
        print("Please enter a number")
        continue


# check if number is the right guess. Otherwise, ask again