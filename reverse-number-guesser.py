#!/usr/bin/python3

import random

print("think of a number between 1-100")
input("press enter when you are ready")

running = True

guess = 0
min = 1
max = 100
guesses = 0

while running:

    guesses += 1

    guess = random.randint(min, max)

    inp = input("is your number " + str(guess) + " ? y/n: ")

    if inp == "y":

        print("haha i won")
        print("guesses: " + str(guesses))

        running = False

    elif min == max:

        print("")
        print("it looks like you are cheating")
        print("i am not going to waste time with a dirty cheater")
        print("goodbye")
        print("")
        print("cheater...")

        running = False

    else:

        inp = input("is your number bigger or smaller? b/s: ")

        if inp == "b":

            min = guess

        elif inp == "s":

            max = guess

    print("")

