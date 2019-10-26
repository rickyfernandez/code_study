def length_of_longest_substring(s):
    j = 0
    sub = []
    sub.append(s[0])

    for i in range(1, len(s)):
        if s[i] not in sub[j]:
            sub[j] = sub[j] + s[i]
        else:
            sub.append(s[i])
            j += 1

    sub_max = len(sub[0])
    for i in range(1, len(sub)):
        if len(sub[i]) > sub_max:
            sub_max = len(sub[i])
    return sub_max

if __name__ == "__main__":
    s = "dvdf"
    print(s, length_of_longest_substring(s))
