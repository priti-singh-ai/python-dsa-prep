class Solution():
    """
    I have tried using DFS
    Problem: The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.
The length of a path between two nodes in a binary tree is the number of edges between the nodes.
 Note that the path can not include the same node twice.

Given the root of a binary tree root, return the diameter of the tree.

Difficulty: Easy
Pattern: Depth first search, breadth first search, binary tree

Time Complexity: O(n)
Space Complexity: O(n)
    
    
    
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            nonlocal res
            res = max(res, left+right)
            return (1+max(left, right))
        dfs(root)
        return res