from utils import *

def cyclically_right_shift_list(node:ListNode, k:int):
    # find the lenght of the list
    list_len = 1
    head = tail = node
    while tail.next:
        tail = tail.next
        list_len += 1

    k = k % list_len
    tail.next = head

    # find new tail
    cur = ListNode(0, head)
    for i in range(k-1):
        cur = cur.next

    head = cur.next
    cur.next = None
    return head

if __name__ == "__main__":
    n = create_nodes([2,3,5,3,2])
    print("Initial")
    print_nodes(n)
    print("Final")
    print_nodes(cyclically_right_shift_list(n, 3))
