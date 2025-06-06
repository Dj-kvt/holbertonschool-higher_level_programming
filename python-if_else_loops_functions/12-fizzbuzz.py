#!/usr/bin/python3
def fizzbuzz():
    """Print the numbers from 1 to 100, but for multiples of three print
    Fizz instead of the number and for the multiples of five print Buzz.
    For numbers which are multiples of both three and five print FizzBuzz.
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=' ')
        elif i % 3 == 0:
            print("Fizz", end=' ')
        elif i % 5 == 0:
            print("Buzz", end=' ')
        else:
            print(i, end=' ')
