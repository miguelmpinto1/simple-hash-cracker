from itertools import product 

def bruteforce(charset, max_size):
    for i in range(1, max_size + 1):
        for combination in product(charset, repeat=i):
            result = "".join(combination)
            yield result