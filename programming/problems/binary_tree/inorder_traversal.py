from utils import BinaryTreeNode

def inorder_traversal(root:BinaryTreeNode):
    current, stack = root, []
    while True:
        if current:
            stack.append(current)
            current = current.left

        elif len(stack):
            current = stack.pop()
            print(current.data)
            current = current.right

        else:
            break

if __name__ == "__main__":

    root = BinaryTreeNode(6)

    # left side of the tree
    root.left = BinaryTreeNode(271)
    root.left.left= BinaryTreeNode(28)
    root.left.right= BinaryTreeNode(0)

    root.right = BinaryTreeNode(561)
    root.right.right = BinaryTreeNode(3)
    root.right.right.left = BinaryTreeNode(17)

    inorder_traversal(root)
