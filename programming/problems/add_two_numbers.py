class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def list_to_number(node):
    val = ""
    while node:
        val = str(node.val) + val
        node = node.next
    return int(val)

def add_two_numbers(l1, l2):
    val1 = list_to_number(l1)
    val2 = list_to_number(l2)

    val = str(val1 + val2)[::-1]
    node0 = ListNode(val[0])
    node = node0

    for i in range(1, len(val)):
        node.next = ListNode(val[i])
        node = node.next
    return node0

if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    l = add_two_numbers(l1, l2)
    print(list_to_number(l))
