# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rec(self, root):
        if root == None:
            return (0,0)
        (left_ht, maxdl) = self.rec(root.left)
        (right_ht, maxdr) = self.rec(root.right)
        if left_ht + right_ht + 1 > max(maxdl, maxdr):
            maxd = left_ht + right_ht + 1
        else:
            maxd = max(maxdl, maxdr)
        return (1 + max(left_ht, right_ht), maxd)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        (max_ht, maxd) = self.rec(root)
        return maxd - 1