
def dec_to_bin(number):
    binary = ""
    while True:
        r = number % 2
        number = number // 2
        binary = binary + str(r)

        if number == 0:
            break
    return binary[::-1]

def dec_to_bin2(n):
    if n<2: return str(n)
    else:
        return dec_to_bin2(n//2) + dec_to_bin2(n%2)

if __name__ == "__main__":
    x = 5
    print(x, dec_to_bin2(x))
