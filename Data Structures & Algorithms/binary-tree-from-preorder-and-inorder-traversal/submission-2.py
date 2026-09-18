# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_check = {}
        for i in range(len(inorder)):
            in_check[inorder[i]] = i

        pre_count = 0
        def helper(in_left, in_right):
            nonlocal in_check
            nonlocal pre_count
            if in_left > in_right:
                return None
            root = TreeNode(preorder[pre_count])
            pre_count += 1
            in_root = in_check[root.val]

            left_in = in_root - 1

            right_in = in_root + 1

            root.left = helper(in_left, left_in)
            root.right = helper(right_in, in_right)
            return root
        return helper(0, len(inorder) - 1)

        



        