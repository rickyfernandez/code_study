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

def add_two_numbers(n1, n2):
    carry = 0
    head = cur = ListNode(0)
    while n1 or n2 or carry:
        val = carry + (n1.data if n1 else 0) + (n2.data if n2 else 0)
        cur.next = ListNode(val % 10)
        carry = val // 10

        n1 = n1.next if n1 else None
        n2 = n2.next if n2 else None
        cur = cur.next

    return head.next

if __name__ == "__main__":
    n1 = create_nodes([3, 1, 4])
    n2 = create_nodes([7, 0, 9])
    n = add_two_numbers(n1, n2)
    print_nodes(n)
