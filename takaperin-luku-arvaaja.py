#!/usr/bin/python3

import random

print("ajattele lukua 1-100")
input("paina enter kun olet valmis")

running = True

guess = 0
min = 1
max = 100
guesses = 0

while running:

    guesses += 1

    guess = random.randint(min, max)

    inp = input("onko lukusi " + str(guess) + " ? k/e: ")

    if inp == "k":

        print("hahaa voitin")
        print("arvaukset: " + str(guesses))

        running = False

    elif min == max:

        print("")
        print("tilanne näyttää siltä että huijaat")
        print("en viitsi tuhlata aikaani likaisten huijarien kanssa")
        print("hyvästi")
        print("")
        print("huijari...")

        running = False

    else:

        inp = input("onko lukusi isompi vai pienempi? i/p: ")

        if inp == "i":

            min = guess

        elif inp == "p":

            max = guess

    print("")

