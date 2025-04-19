import math


def factor(number):
    factor = 2
    # A function to find prime factors of a number
    while factor * factor <= number:
        while number % factor == 0:
            yield factor
            number = number // factor
        factor += 1
    if number > 1:
        yield number


print(list(factor(10)))
