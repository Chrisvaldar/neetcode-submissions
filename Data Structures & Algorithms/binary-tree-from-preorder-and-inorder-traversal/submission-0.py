# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        in_root = inorder.index(root.val)

        left_in = inorder[:in_root]
        left_pre = preorder[1:len(left_in) + 1]

        right_in = inorder[in_root + 1:]
        right_pre = preorder[len(left_in) + 1:]

        root.left = self.buildTree(left_pre, left_in)
        root.right = self.buildTree(right_pre, right_in)
        return root

        



        