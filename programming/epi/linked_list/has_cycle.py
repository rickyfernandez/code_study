from utils import *

def has_cycle(n, start, finish):
    cur = head = ListNode(0, n)
    while cur:
        if head == cur:
            return head
        cur = cur.next
    return None

if __name__ == "__main__":
    n = create_nodes([1, 3, 5, 7, 9])
    print("Initial")
    print_nodes(n)
    print("Final")
    print_nodes(reverse_sublist(n, 2, 4))

