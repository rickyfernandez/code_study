from typing import Deque
import collections

class Queue:
    def __init__(self) -> None:
        self._data: Deque[int] = collections.deque()

    def enqueue(self, x: int) -> None:
        self._data.append(x)

    def dequeue(self) -> int:
        return self._data.popleft()

    def max(self) -> int:
        return max(self._data)

if __name__ == "__main__":
    q = Queue()
    x = [3, 1, 7, 4]
    for val in x:
        q.enqueue(val)

    print(f"input: {x}")

    for i in range(len(x)):
        print(f"Pop value: {q.dequeue()}")
