class BinaryTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def create_tree(arr):
    def _create(node, index):
        if node is None or index >= len(arr):
            return index

        node.left,  index = BinaryTreeNode(arr[index]), index+1
        node.right, index = BinaryTreeNode(arr[index]), index+1

        index = _create(node.left,  index)
        index = _create(node.right, index)
        return index

    root = BinaryTreeNode(arr[0])
    index = 1

    _create(root, index)
    return root

