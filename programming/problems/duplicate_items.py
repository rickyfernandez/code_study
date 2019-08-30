
def duplicate_items(list_numbers):
    num_set = set()
    num_dup = []

    for val in list_numbers:
        if val in num_set:
            num_dup.append(val)
        else:
            num_set.add(val)
    return sorted(num_dup)

def duplicate_items2(list_numbers):
    dup = []
    list_numbers = sorted(list_numbers)
    for i in range(1, len(list_numbers)):
        if list_numbers[i] == list_numbers[i-1]:
            dup.append(list_numbers[i])
    return dup

if __name__ == "__main__":
    x = [1, 2, 1, 5, 2]
    print(x, duplicate_items2(x))
