class Solution:
    """
Problem: Invert Binary Tree
You are given the root of a binary tree root.
Invert the binary tree and return its root.


Example:
Input: root = [1,2,3,4,5,6,7]

Output: [1,3,2,7,6,5,4]

Difficulty: Easy
Pattern: Tree, Depth First Search, Binary Tree

Time Complexity: O(n)
Space Complexity: O(n)
"""
    def invertTree(self, root:Optional[TreeNode]) -> TreeNode:
        if not root:
            return None

        #swapping children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root