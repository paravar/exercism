def sum_of_multiples(limit, multiples):
    return sum([i for i in range(1, limit) if any(i % m == 0 for m in multiples)])
