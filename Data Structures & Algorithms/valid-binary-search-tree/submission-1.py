# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, minBound, maxBound):
            if not root:
                return True

            if not root.val < maxBound or not root.val > minBound:
                return False

            return dfs(root.left, minBound, root.val) and dfs(root.right, root.val, maxBound)
        return dfs(root, float('-inf'), float('inf'))