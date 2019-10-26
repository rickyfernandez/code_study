
def reverse(s, start, stop):
    if start < stop-1:
        s[start], s[stop-1] = s[stop-1], s[start]
        reverse(s, start+1, stop-1)

if __name__ == "__main__":
    s = [1, 2, 3, 4, 5, 6]
    print(s)
    reverse(s, 0, len(s))
    print(s)
