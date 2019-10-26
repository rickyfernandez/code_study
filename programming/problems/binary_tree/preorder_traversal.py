from utils import BinaryTreeNode

def inorder_traversal(root:BinaryTreeNode):
    current, stack = root, []
    while True:
        if current:
            print(current.data)
            stack.append(current)
            current = current.left

        elif len(stack):
            current = stack.pop()
            current = current.right

        else:
            break

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

    inorder_traversal(root)
