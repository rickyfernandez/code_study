def rerrange(A: list) -> None:
    for i in range(len(A)):
        A[i:i+2] = sorted(A[i:i+2], reverse=bool(i % 2))

if __name__ == "__main__":
    x = [3, 1, 5, 2, 2, 9]
    print(x)
    rerrange(x)
    print(x)
