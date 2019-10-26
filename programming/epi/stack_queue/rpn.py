
def rpn(exp):
    stack = []
    exp = exp.split(",")
    for i in range(len(exp)):
        val = exp[i]
        if val.isnumeric():
            stack.append(int(val))

        else:
            a = stack.pop()
            b = stack.pop()

            if   val == "+": stack.append(a + b)
            elif val == "-": stack.append(a - b)
            elif val == "*": stack.append(a * b)
            elif val == "/": stack.append(a // b)

    return stack.pop()


if __name__ == "__main__":
    exp = "3,4,+,2,*,1,+"
    print(f"expression: {exp} computed: {rpn(exp)} answer{(((3+4)*2)*1)+1}")
