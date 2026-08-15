# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, max_):
        if root == None:
            return
        if root.val >= max_:
            self.goodNodes += 1
        if root.val > max_:
            max_ = root.val
        self.dfs(root.left, max_)
        self.dfs(root.right, max_)

    def goodNodes(self, root: TreeNode) -> int:
        self.goodNodes = 0
        self.dfs(root, float("-infinity"))
        return self.goodNodes