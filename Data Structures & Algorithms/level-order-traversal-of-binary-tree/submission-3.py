# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        q = deque()
        q.append(root)
        counter = 1

        res = []
        level = []
        while q:
            curr = q.popleft()
            level.append(curr.val)

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            
            counter -= 1
            if counter == 0:
                res.append(level)
                level = []
                counter = len(q)
        return res