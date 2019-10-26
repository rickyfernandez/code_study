
class Stack:
    def __init__(self):
        self.data = []

    def empty(self):
        return len(self.data) == 0

    def max(self):
        if not self.empty():
            return self.data[-1][1]
        return None

    def pop(self):
        return self.data.pop()[0]

    def push(self, value):
        self.data.append((value, value if self.empty() else max(value, self.max())))

if __name__ == "__main__":
    s = Stack()
    for i in [4, 1, 11, 15, 9, 32]:
        s.push(i)
        print(s.max())
    s.pop()
    print(s.max())


