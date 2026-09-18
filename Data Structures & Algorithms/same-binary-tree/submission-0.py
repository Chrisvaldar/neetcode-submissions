# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(a,b):
            # if a and b:
            #     if a.val != b.val:
            #         return False
            #     helper(a.left, b.left)
            #     helper(a.right, b.right)
            # elif not a and not b:
            #     return True
            if not a and not b:
                return True
            elif not (a and b):
                return False
            elif a.val != b.val:
                return False
            else:
                return helper(a.left, b.left) and helper(a.right, b.right)

        return helper(p,q)
