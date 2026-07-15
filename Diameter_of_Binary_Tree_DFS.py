"""
Problem: 543. Diameter of Binary Tree

Description:
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.

The length of a path is measured by the number of edges between nodes.


Example:

Input:
        1
       / \
      2   3
     / \
    4   5

Output:
3

Explanation:
The longest path is:
4 -> 2 -> 1 -> 3

The number of edges is 3.


Approach:
---------
Depth First Search (DFS) - Postorder Traversal

For every node, the longest path passing through that node is:

    left subtree height + right subtree height

While calculating the height of every node, we update the maximum diameter.

The DFS function returns the height of the subtree because the parent node only
needs the longest branch from its child.


Algorithm:
----------
1. Initialize a variable `diameter` to store the maximum diameter found.

2. Perform DFS traversal:
    - Calculate the height of the left subtree.
    - Calculate the height of the right subtree.
    - Update diameter using:

          left height + right height

    - Return the height of the current node:

          1 + max(left height, right height)

3. Return the final diameter.


Time Complexity:
----------------
O(n)

We visit every node exactly once.


Space Complexity:
-----------------
O(h)

Where h is the height of the tree.
The recursion stack uses O(h) space.
"""


# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root):

        # Stores the maximum diameter found during DFS
        self.diameter = 0

        def dfs(node):

            # Base case:
            # Empty node has height 0
            if not node:
                return 0

            # Find height of left subtree
            left_height = dfs(node.left)

            # Find height of right subtree
            right_height = dfs(node.right)

            # The longest path passing through the current node is:
            #
            # left subtree height + right subtree height
            #
            # Update the maximum diameter
            self.diameter = max(
                self.diameter,
                left_height + right_height
            )

            # Return height of current subtree
            #
            # +1 represents the current node.
            # We return the larger branch because a path going upward
            # can only continue through one child.
            return 1 + max(left_height, right_height)

        # Start DFS traversal from root
        dfs(root)

        return self.diameter


# Driver code for testing
if __name__ == "__main__":

    solution = Solution()

    # Creating Example Tree:
    #
    #          1
    #         / \
    #        2   3
    #       / \
    #      4   5
    #
    # Expected diameter = 3

    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)


    result = solution.diameterOfBinaryTree(root)

    print("Diameter of Binary Tree:", result)