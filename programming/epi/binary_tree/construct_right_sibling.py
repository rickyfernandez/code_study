from queue import Queue

class BinaryTreeNode:
    def __init__(self, data, left=None, right=None, next=None):
        self.data = data
        self.left = left
        self.right = right
        self.next = next

def construct_right_sibling(tree:BinaryTreeNode):
    def _construct_right_sibling(tree:BinaryTreeNode):
        while node and node.left:
            node.left.next = node.right
            node.right.next = node.next.left if node.next else None
            node = node.next

    while tree and tree.left:
        _construct_right_sibling(tree)
        tree = tree.left

if __name__ == "__main__":

    root = BinaryTreeNode('A')

    # left side of the tree
    root.left = BinaryTreeNode('B')
    root.left.left = BinaryTreeNode('C')

    # right side of the tree
    root.right = BinaryTreeNode('D')
    root.right.left = BinaryTreeNode('E')
    root.right.left.left = BinaryTreeNode('F')
    root.right.right = BinaryTreeNode('G')
    root.right.right.left = BinaryTreeNode('H')
    root.right.right.right = BinaryTreeNode('I')

    construct_right_sibling(root)
