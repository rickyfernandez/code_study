def linear_sum(s, n):
    if n == 0:
        return 0
    else:
        return linear_sum(s, n-1) + s[n-1]

if __name__ == "__main__":
    x = [1, 2, 3]
    print(x, linear_sum(x, len(x)))

