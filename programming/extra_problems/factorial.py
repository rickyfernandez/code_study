
def factorial(n):
    """
    Returns the factorial of n.
    """
    result = factor = n
    while factor > 1:
        factor -= 1
        result *= factor
    return result

def factorial_recursion(n):
    """
    Returns the factorial of n.
    """
    if n == 0:
        return 1
    return n*factorial(n-1)

if __name__ == '__main__':
    x = 3
    print("%d! is: %d" % (x, factorial(x)))
