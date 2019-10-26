from utils import *

def path_sum(tree:BinaryTreeNode, value:int)->bool:
    def _path_sum(tree, path_sum=0):
        if tree is None:
            return False

        s = path_sum + tree.data
        if tree.left is None and tree.right is None:
            return s == value

        return _path_sum(tree.left,  s) or _path_sum(tree.right, s)

    return _path_sum(tree)

if __name__ == "__main__":

    root = BinaryTreeNode(314)

    # left side of the tree
    root.left = BinaryTreeNode(6)
    root.left.left = BinaryTreeNode(271)
    root.left.right = BinaryTreeNode(561)
    root.left.left.left = BinaryTreeNode(28)
    root.left.left.right = BinaryTreeNode(0)
    root.left.right.right = BinaryTreeNode(3)
    root.left.right.right.left = BinaryTreeNode(17)

    # right side of the tree
    root.right = BinaryTreeNode(6)
    root.right.left = BinaryTreeNode(2)
    root.right.left.right = BinaryTreeNode(1)
    root.right.left.right.left = BinaryTreeNode(401)
    root.right.left.right.right = BinaryTreeNode(257)
    root.right.left.right.left.right = BinaryTreeNode(641)
    root.right.right = BinaryTreeNode(271)
    root.right.right.right = BinaryTreeNode(28)

    # path to N
    print(path_sum(root, 580))
