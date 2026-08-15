# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root):
        if root == None:
            return 0
        maxSumL = self.dfs(root.left)
        maxSumR = self.dfs(root.right)
        maxSum = max(root.val, root.val + maxSumL, root.val + maxSumR)
        maxPath = root.val
        if maxSumL > 0:
            maxPath += maxSumL
        if maxSumR > 0:
            maxPath += maxSumR
        if maxPath > self.maxPathSum:
            self.maxPathSum = maxPath
        return maxSum
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPathSum = float("-infinity")
        self.dfs(root)
        return self.maxPathSum