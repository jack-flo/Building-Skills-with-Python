# Sieve of Eratosthenes with sets instead.
bound = 5000
prime = set(range(2, bound))
p = 2

while 2 <= p < bound:
    # this checks to find values that are still in the list (only the prime values will be left behind)
    while p not in prime and p < bound:
        p += 1
    # This creates a set of values p between 2 and the bound
    multiples = set(range(p*2, bound, p))
    # this removes all the multiples of p at once from prime
    prime.difference_update(multiples)
    p += 1

print(prime)
