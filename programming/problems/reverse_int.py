
def reverse_int(x):
    # 64 bit with one valued used for zero
    # one power used for negative
    int_max =  2**31-1
    int_min = -2**31

    rev = 0
    sign = 1

    if int_min > x or x > int_max:
        return 0

    if x < 0:
        # convert to positive number
        sign = -1
        x *= sign

    while x != 0:
        # strip last digit and
        # move to next digit
        pop = x % 10
        x = x // 10

        rev = rev*10 + pop

    if int_min > rev or rev > int_max:
        return 0

    return sign*rev

if __name__ == "__main__":
    x = -5763920
    print(x, reverse_int(x))
