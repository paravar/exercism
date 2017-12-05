"""
def sieve(limit):
    prime_list = list()
    if limit == 0 or limit == 1:
        return prime_list
    ls = [True] * (limit+1)
    ls[0], ls[1] = False, False
    for i, isprime in enumerate(ls):
        if isprime:
            prime_list.append(i)
            for n in range(i, limit+1, i):
                ls[n] = False
    return prime_list
"""


def sieve(limit):
    multiples = []
    primes = []
    for i in range(2, limit+1):
        if i not in multiples:
            primes.append(i)
            multiples += [j for j in range(i**2, limit+1, i)]
    return primes
