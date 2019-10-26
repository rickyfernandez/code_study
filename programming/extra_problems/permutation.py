
def permutation(str1, str2):
    "check if str1 is a permutation of the other"
    n1 = len(str1)
    n2 = len(str2)

    if n1 != n2:
        return False

    str1 = sorted(str1)
    str2 = sorted(str2)

    for i in range(n1):
        if str1[i] != str2[i]:
            return False
    return True

def permutation2(str1, str2):
    "check if str1 is a permutation of the other"
    n1 = len(str1)
    n2 = len(str2)
    if n1 != n2:
        return False

    freq = [0]*128
    for i in range(n1):
        val = ord(str1[i]) - ord("a")
        freq[val] += 1

    for i in range(n2):
        val = ord(str2[i]) - ord("a")
        freq[val] -= 1
        if freq[val] < 0:
            return False

    return True
if __name__ == "__main__":
    x = "cat"
    y = "tac"
    print(x, y, permutation2(x, y))

    x = "cat"
    y = "tab"
    print(x, y, permutation2(x, y))
