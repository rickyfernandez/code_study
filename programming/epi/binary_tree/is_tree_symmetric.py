from utils import BinaryTreeNode

def is_tree_symmetric(root:BinaryTreeNode):
    def _is_tree_symmetric(left:BinaryTreeNode, right:BinaryTreeNode):
        if left is None and right is not None:
            return False

        if left is not None and right is None:
            return False

        if left is None and right is None:
            return True

        if left.data != right.data:
            return False

        return _is_tree_symmetric(left.left, right.right) and _is_tree_symmetric(left.right, right.left)

    return _is_tree_symmetric(root.left, root.right)

if __name__ == "__main__":

    root = BinaryTreeNode(314)

    # left side of the tree
    root.left = BinaryTreeNode(6)
    root.left.right = BinaryTreeNode(2)
    root.left.right.right = BinaryTreeNode(3)

    root.right = BinaryTreeNode(6)
    root.right.left = BinaryTreeNode(2)
    root.right.left.left = BinaryTreeNode(3)

    print(is_tree_symmetric(root))
