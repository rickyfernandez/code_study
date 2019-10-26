import numpy as np

def generate_primes1(n: int) -> list:
    primes = [False, False] + [True]*(n-1)
    for i in range(2, n+1):
        for j in range(2, int(np.sqrt(i)) + 1):
            if i % j == 0:
                primes[i] = False
                break

    return [i for i in range(n) if primes[i]]

def generate_primes2(n: int) -> list:
    if n < 2:
        return []

    primes = []
    is_prime = [False, False] + [True]*(n-1)
    for i in range(2, n+1):
        if is_prime[i]:
            primes.append(i)

            for j in range(2*i, n+1, i):
                is_prime[j] = False

    return primes

if __name__ == "__main__":
    n = 45
    print(n, generate_primes2(n))
