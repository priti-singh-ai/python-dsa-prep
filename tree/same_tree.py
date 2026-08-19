class Solution:
    """Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.
    Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.
    Difficulty: Easy
    Pattern: Depth first search, breadth first search, binary tree

    Time Complexity: O(n)
    Space Complexity: O(n)
"""
    def isSameTree(self, p:Optional[TreeNode], q:Optional[TreeNode]) -> bool:

        def dfs(p,q):
            if not p and not q:
                return True
            elif not p or not q or p.val != q.val:
                return False
            return dfs(p.left,q.left) and dfs(p.right,q.right)

        return dfs(p,q)