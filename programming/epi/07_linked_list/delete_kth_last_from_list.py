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

def delete_kth_last_from_list(node, k):
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
