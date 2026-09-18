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
        res = []
        temp = []
        queue = deque()
        queue.append(root)

        checkLen = 1
        counter = 0
        while queue:
            curr = queue.popleft()
            counter += 1
            temp.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            
            if counter == checkLen:
                checkLen = len(queue)
                counter = 0
                res.append(temp)
                temp = []
        
        return res
            
