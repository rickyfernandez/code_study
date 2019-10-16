from utils import *

def reverse_sublist(node:ListNode, start:int, finish:int):
    prev = head = ListNode(0, node)
    for i in range(1, start):
        prev = prev.next

    cur = prev.next
    for i in range(finish - start):
        temp = cur.next

        cur.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return head.next

if __name__ == "__main__":
    n = create_nodes([1, 3, 5, 7, 9])
    print("Initial")
    print_nodes(n)
    print("Final")
    print_nodes(reverse_sublist(n, 2, 4))
