# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = k
        res = 0
        def helper(curr):
            nonlocal counter
            nonlocal res
            if not curr:
                return

            helper(curr.left)
            if counter == 0:
                return
            counter -= 1
            if counter == 0:
                res = curr.val
                return
            helper(curr.right)
        helper(root)
        return res
