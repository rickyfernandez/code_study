
def sorted_array_remove_dups(A: list) -> int:
    if not A:
        return 0

    index = 1
    for i in range(1, len(A)):
        if A[i] != A[i-1]:
            A[index] = A[i]
            index += 1
    return index

if __name__ == "__main__":
    x = [1, 2, 2, 3, 4, 5, 5, 6, 6]
    print(x)
    sorted_array_remove_dups(x)
    print(x)

