import math


def factor(number):
    factor = 2
    # A function to find prime factors of a number
    while factor * factor <= number:
        if number % factor == 0:
            yield factor
            number = number // factor
        factor += 1
    if number > 1:
        yield number


print(list(factor(10)))

# FUNCTION factor(n):
#     # Start trial divisor at the smallest prime
#     SET f ← 2

#     # As long as f² ≤ n, test f as a factor
#     WHILE f * f ≤ n DO
#         # While f divides n with no remainder, it’s a prime factor
#         WHILE n MOD f = 0 DO
#             OUTPUT f
#             SET n ← n ÷ f
#         END WHILE

#         # Move on to the next potential factor
#         # (you could skip even numbers after f=2 if you like)
#         SET f ← f + 1
#     END WHILE

#     # If n is now > 1, what remains must itself be prime
#     IF n > 1 THEN
#         OUTPUT n
#     END IF
# END FUNCTION
