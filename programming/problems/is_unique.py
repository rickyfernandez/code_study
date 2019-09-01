
def is_unique(string):
    string = sorted(string)
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            return False
    return True

def is_unique2(string):
    mask = 0
    for i in range(len(string)):
        val = ord(string[i]) - ord("a")
        if mask & (1 << val):
            return False
        mask = mask | (1 << val)
    return True

if __name__ == "__main__":
    x = "carpet"
    print(x, is_unique2(x))
    x = "muppet"
    print(x, is_unique2(x))

