# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rec(self, root):
        if root == None:
            return (0, True)
        left_ht, is_left_bal = self.rec(root.left)
        if is_left_bal == False:
            return (-1, False)

        right_ht, is_right_bal = self.rec(root.right)
        if is_right_bal == False:
            return (-1, False)

        if abs(left_ht - right_ht) < 2:
            return (1 + max(left_ht, right_ht), True)
        else:
            return (-1, False)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ht, is_Bal = self.rec(root)
        return is_Bal
        
        