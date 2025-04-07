# Creating an algorithm to find all the prime numbers within a given bound

bound = 5000
prime = [True] * bound
p = 2

# whilst the number is between 2 and the bound
while 2 <= p < bound:
    # while the value is not prime and between the bound
    while not prime[p] and 2 <= p < bound:
        p += 1
    # gets double the prime (not a prime)
    k = p + p

    while k < bound:
        # getting rid of all values that are multiples of the prime number
        prime[k] = False
        k += p

    p += 1

amount = 0
# Display the prime numbers
for number in range(2, bound):
    if prime[number]:
        print(number, end=" ")
        amount += 1

print((amount / bound) * 100)
