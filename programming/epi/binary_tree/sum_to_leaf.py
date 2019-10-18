from utils import *

def sum_to_root(tree:BinaryTreeNode):
    def _sum_to_root(tree, path_sum=0):
        if tree is None:
            return 0

        val = 2*path_sum + tree.data
        if tree.left is None and tree.right is None:
            return val

        return _sum_to_root(tree.left, val) + _sum_to_root(tree.right, val)

    return _sum_to_root(tree)

if __name__ == "__main__":

    root = BinaryTreeNode(1)

    # left side of the tree
    root.left = BinaryTreeNode(0)
    root.left.left = BinaryTreeNode(0)
    root.left.left.left = BinaryTreeNode(0)
    root.left.right = BinaryTreeNode(1)
    root.left.right.right = BinaryTreeNode(1)
    root.left.right.right.left = BinaryTreeNode(0)

    # right side of the tree
    root.right = BinaryTreeNode(1)
    root.right.right = BinaryTreeNode(0)
    root.right.right.right = BinaryTreeNode(0)
    root.right.left = BinaryTreeNode(0)
    root.right.left.right = BinaryTreeNode(0)
    root.right.left.right.right = BinaryTreeNode(0)
    root.right.left.right.left = BinaryTreeNode(1)
    root.right.left.right.left.right = BinaryTreeNode(1)

    print(sum_to_root(root))
