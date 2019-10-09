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

def list_pivot(l, x):
    head_less = tail_less = ListNode(0)
    head_equal = tail_equal = ListNode(0)
    head_greater = tail_greater = ListNode(0)

    while l:
        if l.data < k:
            tail_less.next = l
            tail_less = tail_less.next
        elif l.data > k:
            tail_greater.next = l
            tail_greater = tail_greater.next
        else:
            tail_equal.next = l
            tail_equal = tail_equal.next
        l = l.next

    tail_less.next = head_equal.next
    tail_equal.next = head_greater.next

    return head_less.next

if __name__ == "__main__":
    k = 7
    n = create_nodes([3, 2, 2, 11, 7, 5, 11])
    print("Initial")
    print_nodes(n)
    print("Final")
    print_nodes(list_pivot(n, k))
