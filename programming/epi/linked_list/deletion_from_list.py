from utils import *

def deletion_from_list(n):
    n.data = n.next.data
    n.next = n.next.next

if __name__ == "__main__":
    n = create_nodes([1, 3, 5, 7, 9])
    print("Initial")
    print_nodes(n)
    print("Final")
    deletion_from_list(n)
    print_nodes(n)
