# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxVal):
            currMax = maxVal
            res = 0
            if not root:
                return 0
            if root.val >= currMax:
                currMax = root.val
                res = 1
            
            return res + dfs(root.left, currMax) + dfs(root.right, currMax)
        
        return dfs(root, root.val)
            