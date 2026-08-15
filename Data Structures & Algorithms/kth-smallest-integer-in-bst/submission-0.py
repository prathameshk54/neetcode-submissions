# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, k):
        if root == None:
            return
        self.dfs(root.left, k)
        self.count += 1
        if self.count == k:
            self.res = root.val
            return
        self.dfs(root.right, k)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.res = 0
        self.dfs(root, k)
        return self.res
        