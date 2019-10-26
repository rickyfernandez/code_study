from utils import BinaryTreeNode

def is_tree_balanced(root:BinaryTreeNode):
    class BalancedHeigth:
        def __init__(self, balanced, height):
            self.balanced = balanced
            self.height = height

    def _is_tree_balanced(node:BinaryTreeNode):
        if node is None:
            return BalancedHeigth(True, -1)

        left_res = _is_tree_balanced(node.left)
        if not left_res.balanced:
            return BalancedHeigth(False, 0)

        right_res = _is_tree_balanced(node.right)
        if not left_res.balanced:
            return BalancedHeigth(False, 0)

        balanced = abs(right_res.height - left_res.height) <= 1
        height   = max(right_res.height,  left_res.height) + 1
        return BalancedHeigth(balanced, height)

    return _is_tree_balanced(root).balanced

if __name__ == "__main__":

    root = BinaryTreeNode("A")

    # left side of the tree
    root.left = BinaryTreeNode("B")
    root.left.left = BinaryTreeNode("C")
    root.left.right = BinaryTreeNode("H")
    root.left.left.left = BinaryTreeNode("D")
    root.left.left.right = BinaryTreeNode("G")
    root.left.right.left = BinaryTreeNode("I")
    root.left.right.right = BinaryTreeNode("J")

    # right side of the tree
    root.right = BinaryTreeNode("K")
    root.right.right = BinaryTreeNode("O")
    root.right.left = BinaryTreeNode("L")
    root.right.left.right = BinaryTreeNode("N")
    root.right.left.left = BinaryTreeNode("M")

    print(is_tree_balanced(root))
