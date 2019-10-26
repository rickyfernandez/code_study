def power(x, n):
    if n < 2:
        return x
    else:
        return x * power(x, n-1)

def power2(x, n):
    if n == 0:
        return 1
    else:
        partial = power2(x, n//2)
        result = partial * partial
        if n%2 == 1:
            result *= x
        return result

if __name__ == "__main__":
    x = 2; n = 13
    print(x, n, power2(x, n))
