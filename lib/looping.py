#!/usr/bin/env python3
def happy_new_year():
    countdown = 10

    while countdown > 0:
        print(countdown)
        countdown -= 1

    print("Happy New Year!")


happy_new_year()


def square_integers(numbers):
    squared_numbers = [num ** 2 for num in numbers]
    return squared_numbers


def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


fizzbuzz()
