#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")

def square_integers(int_list):
    int_list_squared = [i * i for i in int_list]
    return int_list_squared

def fizzbuzz():
    for i in range(1, 101):
        if (i / 3 == int(i / 3)) and (i / 5 == int(i / 5)):
            print("FizzBuzz")
        elif i / 3 == int(i / 3):
            print("Fizz")
        elif i / 5 == int(i / 5):
            print("Buzz")
        else:
            print(i)
