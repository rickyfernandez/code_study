from utils import *

def merge_two_sorted_lists(n1:ListNode, n2:ListNode):
    head = curr = ListNode()
    while n1 and n2:
        if n1.data < n2.data:
            curr.next = n1
            n1 = n1.next
        else:
            curr.next = n2
            n2 = n2.next
        curr = curr.next

    curr.next = n1 if n1 else n2
    return head.next

if __name__ == "__main__":
    n1 = create_nodes([2, 5, 7])
    n2 = create_nodes([3, 11])
    print_nodes(merge_two_sorted_lists(n1, n2))
