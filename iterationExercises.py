import random

# Greatest common divisor


def findGCD(x, y):
    while y != 0:
        x, y = y, x % y
        print(x, y)
    return x


num1, num2 = 28, 21
print(f"The GCD of {num1} and {num2} is {findGCD(num1, num2)}")

# Extracting the Square Root


# def findSquareRoot(n):
#     x = 0
#     while (x * n - n) / n < 0.001:
#         mid = (x + n) / 2
#         cmp = mid * mid - n
#         print(mid)
#         if cmp < 0:
#             x = mid
#         elif cmp > 0:
#             n = mid
#         elif cmp == 0:
#             return mid

def findSquareRoot(n):
    low = 0
    high = n

    while (high - low) > 0.001:
        mid = (low + high) / 2
        # Mid squared vs target nunber
        if mid * mid < n:
            low = mid
        else:
            high = mid

    mid = round((low + high) / 2, 2)
    return mid


print(findSquareRoot(49))

# Highest power of two
# Given a number, n, find a number p such that 2^p <= n < 2^p+1
# Use the << operator
# This can be done with only addition and multiplication by 2


def highestPower(n):
    p = 1
    c = 2
    # Find the lower bound
    while c * 2 < n:
        p += 1
        c = c * 2
    print(f"p is equal to {p} such that 2^{p} <= {n} < 2^{p + 1}")


highestPower(49)


# Hailstone numbers


def generateHailstonePaths():
    pathDistance = 0
    for i in range(2, 31):
        x = i
        while x != 1:
            if x % 2 == 1:
                x = x * 3 + 1
                pathDistance += 1
            else:
                x = x // 2
                pathDistance += 1
        print(f"The path distance for {i} is {pathDistance}")
        pathDistance = 0


generateHailstonePaths()
