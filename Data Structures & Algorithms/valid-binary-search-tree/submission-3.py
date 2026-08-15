# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root):
        min_ = root.val
        max_ = root.val

        if root.left:
            minL, maxL, isBalL = self.dfs(root.left)
            if minL < min_:
                min_ = minL
            if maxL > max_:
                max_ = maxL
            isBalL = isBalL and maxL < root.val
        else:
            isBalL = True

        if root.right:
            minR, maxR, isBalR = self.dfs(root.right)
            if minR < min_:
                min_ = minR
            if maxR > max_:
                max_ = maxR
            isBalR = isBalR and minR > root.val
        else:
            isBalR = True
        
        if isBalL and isBalR:
            return (min_, max_, True)
        else:
            return (min_, max_, False)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[2]

        