from utils import *

def reverse_list(node:ListNode):
    head = curr = node
    while curr.next:

        temp = curr.next
        curr.next = temp.next

        temp.next = head
        head = temp

    return head

if __name__ == "__main__":
    n = create_nodes([1, 3, 5, 7, 9])
    print("Initial")
    print_nodes(n)
    print("Final")
    print_nodes(reverse_list(n))

