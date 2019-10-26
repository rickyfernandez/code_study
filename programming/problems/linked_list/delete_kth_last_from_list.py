from utils import *

def delete_kth_last_from_list(node:ListNode, k):
    runner = head = node
    for i in range(k):
        runner = runner.next

    cur = head
    while runner.next:
        cur = cur.next
        runner = runner.next
    cur.next = cur.next.next
    return head

if __name__ == "__main__":
    n = create_nodes([2, 5, 7, 11, 3, 2, 10])
    print("Initial")
    print_nodes(n)
    print("Final")
    print_nodes(delete_kth_last_from_list(n, 3))
