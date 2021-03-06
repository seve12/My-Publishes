#!/usr/bin/python3

import random
import time
import math
#import turtle
#import winsound
#import tkinter as tk

# CALCULATOR APP

def calculator():
    running = True

    while running:
        asking = True
        while asking:
            var1 = input("enter first variable: ")
            if var1.isdecimal():
                asking = False
            else:
                print("ERROR Please input a number")
        asking = True
        while asking:
            calc = input("enter calculation (+,-,*,/): ")
            if calc == "+" or calc == "+" or calc == "*" or calc == "/":
                asking = False
            else:
                print("ERROR Please enter a valid calculation")

        asking = True

        while asking:
            var2 = input("enter second variable: ")
            if var2.isdecimal():
                asking = False
            else:
                print("ERROR Please input a number")

        var1 = float(var1)
        var2 = float(var2)

        if calc == "+":
            ans = var1 + var2
            print("answer: " + str(ans))
        elif calc == "-":
            ans = var1 - var2
            print("answer: " + str(ans))
        elif calc == "/":
            ans = var1 / var2
            print("answer: " + str(ans))
        elif calc == "*":
            ans = var1 * var2
            print("answer: " + str(ans))
        if input("quit? y/n: ") == "y":
            running = False

# TIMER APP

def timer():
    running = True
    while running:
        if input("activate beepmode (y/n): ") == "y":
            beepmode = True
        else:
            beepmode = False
        timer = input("enter amount of time: ")
        timer = int(timer)

        while timer >= 1:
            if beepmode == True:
                winsound.Beep(500, 100)
            print(timer)
            time.sleep(1)
            timer -= 1
        print("Done")
        #winsound.PlaySound("alarm.wav", winsound.SND_FILENAME)

        if input("quit? y/n: ") == "y":
            running = False

# FILE EDITOR

def file_editor():
    running = True
    while running:
        print("1 = new file/overwrite")
        print("2 = add to the end of the file")
        print("3 = read file")
        print("Q = quit")

        select = input("")
        if select == "1":
            f = open("text.txt", "w")
            wrt = input("input text: ")
            f.write(wrt)
            f.close()
        elif select == "2":
            f = open("text.txt", "a")
            wrt = input("input text: ")
            f.write(wrt + "\n")
            f.close()
        elif select == "3":
            f = open("text.txt")
            lines = f.readlines()
            for line in lines:
                print(line)
        elif select == "Q":
            running = False

# TURTLE DRAWING PROGRAM

def turtle_drawer():
    running = True
    t = turtle.Turtle()
    while running:
        print("F = forward")
        print("B = backward")
        print("L = left")
        print("R = right")
        print("Q = quit")
        inp = input("input command: ")

        if inp[0] == "F":
            if inp[1:].isdecimal():
                t.forward(int(inp[1:]))
            else:
                print("please input a value")

        if inp[0] == "B":
            if inp[1:].isdecimal():
                t.backward(int(inp[1:]))
            else:
                print("please input a value")

        if inp[0] == "L":
            if inp[1:].isdecimal():
                t.left(int(inp[1:]))
            else:
                print("please input a value")
        if inp[0] == "R":
            if inp[1:].isdecimal():
                t.right(int(inp[1:]))
            else:
                print("please input a value")
        if inp == "N":
            t.clear()
        if inp == "U":
            t.penup()
        if inp == "D":
            t.pendown()
        if inp == "Q":
            running = False


# NEW APP

def APP():
    running = True
    while running:
        # code goes here
        if input("quit? y/n: ") == "y":
            running = False

# MAIN CODE

salasana = ""

#if input("enter password: ") == str(salasana):
if input("press enter: ") == str(salasana):
    # LOOP
    while True:
        print("welcome to SeveOS")
        print("1 = calculator")
        print("2 = timer")
        print("3 = file editor")
        print("4 = turtle drawing")

        select = input()

        # APP SELECT
        if select == "1":
            calculator()
        elif select == "2":
            timer()
        elif select == "3":
            file_editor()
        elif select == "4":
            turtle_drawer()
