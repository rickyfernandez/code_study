
def is_well_formed(exp):
    stack = []
    table = {"(": ")", "{": "}", "[": "]"}
    for char in exp:
        if char in "[({":
            stack.append(char)
        else:
            if table[stack.pop()] != char:
                return False
    return len(stack) == 0

if __name__ == "__main__":
    exp = "[()[]{()()}]"
    print(f"Expression: {exp} is well formed: {is_well_formed(exp)}")
