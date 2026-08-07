class Solution:
    """
Problem: Maximum Depth of a binary Tree
Given the root of a binary tree, return its depth.

The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.



Difficulty: Easy
Pattern: Depth first search, breadth first search, binary tree

Time Complexity: O(n)
Space Complexity: O(n)
"""
    def maxDepth(self, root:[rootNode]) -> int:
        if root is None:
            return 0
        return 1+ max(self.maxDepth(root.left),self.maxDepth(root.right))