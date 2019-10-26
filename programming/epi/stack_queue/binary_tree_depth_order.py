from typing import List
from ..binary_tree.utils import BinaryTreeNode

def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    result: List[List[int]] = []
    if not tree:
        return result

    curr_depth_nodes = [tree]
    while curr_depth_nodes:
        result.append([node.data for node in curr_depth_nodes])
        curr_depth_nodes = [child for node in curr_depth_nodes
                for child in (node.left, node.right) if child]
    return result

if __name__ == "__main__":

    root = BinaryTreeNode(1)

    # left side of the tree
    root.left = BinaryTreeNode(2)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)

    # right side of the tree
    root.right = BinaryTreeNode(3)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)
    root.right.right.right = BinaryTreeNode(9)
    print(binary_tree_depth_order(root))
