from typing import Optional


def create_nodes(arr):
    head = curr = ListNode()
    for a in arr:
        curr.next = ListNode()
        curr.next.data = a
        curr = curr.next
    return head.next

def print_nodes(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def deletion_from_list(n):
    n.data = n.next.data
    n.next = n.next.next


if __name__ == "__main__":
    n = create_nodes([1, 3, 5, 7, 9])
    print("Initial")
    print_nodes(n)
    print("Final")
    print_nodes(reverse_list(n))

