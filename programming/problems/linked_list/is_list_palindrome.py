from utils import *
from reverse_list import reverse_list

def is_linked_list_a_palindrome(head:ListNode)->bool:
    head = mid = tail = n
    while mid and tail.next:
        mid  = mid.next
        tail = tail.next.next

    mid = reverse_list(mid)
    while mid and head:
        if mid.data != head.data:
            return False
        mid, head = mid.next, head.next
    return True

if __name__ == "__main__":
    string = "h,a,n,n,a,h,a"
    print(string)
    n = create_nodes(string.split(','))
    print("is palindrome", is_linked_list_a_palindrome(n))

