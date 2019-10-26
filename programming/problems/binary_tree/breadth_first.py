from utils import BinaryTreeNode
from queue import Queue

def breadth_first(root:BinaryTreeNode):
    current, q = root, Queue()
    q.put(root)
    while True:
        if not q.empty():
            node = q.get()
            print(node.data)

            if node.left:  q.put(node.left)
            if node.right: q.put(node.right)
        else:
            break

if __name__ == "__main__":

    root = BinaryTreeNode(1)

    # left side of the tree
    root.left = BinaryTreeNode(2)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)

    # right side of the tree
    root.right = BinaryTreeNode(3)
    breadh_first(root)
