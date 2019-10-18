from utils import *

def lca(tree:BinaryTreeNode, node0:BinaryTreeNode, node1:BinaryTreeNode):
    def _lca(tree, node0, node1):
        if tree is None:
            return 0, None

        left_count, left_node = _lca(tree.left, node0, node1)
        if left_count == 2:
            return (left_count, left_node)

        right_count, right_node = _lca(tree.right, node0, node1)
        if right_count == 2:
            return (right_count, right_node)

        count = 0
        if tree is node0: count += 1
        if tree is node1: count += 1

        count = left_count + right_count + count
        node = tree if count == 2 else None
        return count, node

    _, node = _lca(tree, node0, node1)
    return node

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
    root.right.left.right.right = node1 = BinaryTreeNode(257)
    root.right.left.right.left.right = node0 = BinaryTreeNode(641)
    root.right.right = BinaryTreeNode(271)
    root.right.right.right = BinaryTreeNode(28)

    print(lca(root, node0, node1).data)
