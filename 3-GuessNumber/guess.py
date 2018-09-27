# This is a Guess the Number game.
import random

RANGE = [1, 20]
MAX_GUESS_TAKEN = 6

if __name__ == '__main__':
    guessesTaken = 0
    guess = 0

    print("Hello! What is your name?")
    myName = input()

    number = random.randint(RANGE[0], RANGE[1])
    print("Well, " + myName + ", I am thinking of a number between " + str(RANGE[0]) + " and " + str(RANGE[1]) + ".")

    for i in range(MAX_GUESS_TAKEN):
        print("Take a guess.")
        guessesTaken = guessesTaken + 1
        while True:
            try:
                guess = input()
                guess = int(guess)
                break
            except ValueError as e:
                print(str(guess) + " is not a valid guess. Try again.")
                continue

        if guess < number:
            print("Your guess is too low.")

        if guess > number:
            print("Your guess is too high.")

        if guess == number:
            break

    if guess == number:
        guessesTaken = str(guessesTaken)
        print("Good job, " + myName + "! You guessed my number in " + guessesTaken + " guesses!")

    if guess != number:
        number = str(number)
        print("Nope. The number I was thinking of was " + number + ".")
