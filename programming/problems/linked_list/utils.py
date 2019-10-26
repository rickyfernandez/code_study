from typing import List

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def create_nodes(arr:List):
    head = curr = ListNode()
    for a in arr:
        curr.next = ListNode()
        curr.next.data = a
        curr = curr.next
    return head.next

def print_nodes(head:ListNode):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next

