from utils import BinaryTreeNode, is_leaf

def exterior(root:BinaryTreeNode):
    def _left(node:BinaryTreeNode):
        # grab left without left most leaf
        if node is None or is_leaf(node):
            return

        nodes.append(node.data)

        if node.left:
            _left(node.left)
        else:
            _left(node.right)

    def _leafs(node:BinaryTreeNode):
        # grab left without left most leaf
        if node is None:
            return

        if is_leaf(node):
            nodes.append(node.data)
            return

        _leafs(node.left)
        _leafs(node.right)

    def _right(node:BinaryTreeNode):
        # grab left without left most leaf
        if node is None or is_leaf(node):
            return

        if node.right:
            _right(node.right)
        else:
            _right(node.left)

        nodes.append(node.data)

    nodes = [root.data]
    _left(root.left)
    _leafs(root)
    _right(root.right)

    return nodes

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

    print(exterior(root))
