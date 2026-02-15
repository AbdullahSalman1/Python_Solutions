"""
Binary Search Tree (BST) Node Addition

This script demonstrates adding a new node to a BST represented as a dictionary.
Each node is a dictionary with 'value', 'left', and 'right' pointers.

Time Complexity: O(h), where h is the height of the BST
Space Complexity: O(1)
"""

def bst_addition(tree, root, new_val):
    """
    Adds a new value to the BST.

    Args:
        tree (dict): BST represented as a dictionary of nodes
        root (str): Key of the root node
        new_val (int): Value to insert
    """
    node = root
    while True:
        if new_val > tree[node]["value"]:
            side = "right"
        elif new_val < tree[node]["value"]:
            side = "left"
        else:
            # Duplicate value, do nothing
            break

        if tree[node][side] is None:
            # Create new node
            new_key = "node" + str(len(tree))
            tree[node][side] = new_key
            tree[new_key] = {"value": new_val, "left": None, "right": None}
            break
        else:
            node = tree[node][side]



if __name__ == "__main__":
    bst = {
        'root': {'value': 50, 'left': None, 'right': None}
    }
    bst_addition(bst, 'root', 30)
    bst_addition(bst, 'root', 70)
    bst_addition(bst, 'root', 60)
    print("BST after additions:", bst)
