from utils import BinaryTreeNode
from queue import Queue

class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def print_nodes(head:ListNode):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next

def create_list_of_leaves(root:BinaryTreeNode):
    def _create_list_of_leaves(root, node):
        # check if node is a leaf
        if root.left is None and root.right is None:
            node.next = ListNode(root.data)
            node = node.next
            return node

        node = _create_list_of_leaves(root.left,  node)
        node = _create_list_of_leaves(root.right, node)
        return node

    node = head = ListNode(0)
    _create_list_of_leaves(root, node)
    return head.next

if __name__ == "__main__":

    root = BinaryTreeNode(1)

    # left side of the tree
    root.left = BinaryTreeNode(2)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)

    # right side of the tree
    root.right = BinaryTreeNode(3)
    head = create_list_of_leaves(root)

    print_nodes(head)
