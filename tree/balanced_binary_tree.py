class Solution:
    """
    Given a binary tree, return true if it is height-balanced and false otherwise.
    A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
    Difficulty: Easy
    Pattern: Depth first search, breadth first search, binary tree

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    def isBalanced(self, root:Optional[TreeNode]) -> bool:
        def dfs (root):
            if root is None:
                return (True,0)

            left = dfs(root.left)
            right = dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1])<=1)
            return (balanced, 1+max(left[1],right[1]))
        dfs(root)
        return root[0]















            