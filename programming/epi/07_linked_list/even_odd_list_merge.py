from utils import *

def even_odd_merge(node:ListNode):
    even_head = ListNode(0)
    odd_head  = ListNode(0)

    flip = 0
    tails = [even_head, odd_head]
    while node:
        tails[flip].next = node
        tails[flip] = tails[flip].next
        node = node.next
        flip ^= 1
    tails[0].next = odd_head.next
    tails[1].next = None
    return even_head.next

if __name__ == "__main__":
    n = create_nodes(list(range(7)))
    print("Initial")
    print_nodes(n)
    print("Final")
    print_nodes(even_odd_merge(n))
