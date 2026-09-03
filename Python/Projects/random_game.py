from random import randint

def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print("Correct!")
            return True
    else:
        print("Hey, I said 1 - 10!!!")
        return False


if __name__ == '__main__':
    answer = randint(1, 10)
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            if (run_guess(guess, answer)):
                break
        except ValueError:
            print("Please enter a number")
            continue


# check if number is the right guess. Otherwise, ask again