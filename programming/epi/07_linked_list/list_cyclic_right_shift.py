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

def cyclically_right_shift_list(l, k):
    # find the lenght of the list
    list_len = 1
    head = tail = l
    while tail.next:
        tail = tail.next
        list_len += 1

    k = k % list_len
    tail.next = head
    print(head.data, tail.data)

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
