# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        q = deque()
        q.append(root)
        res = []
        lvl_end = 0
        n =  len(q)
        while(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            lvl_end = node.val
            n -= 1
            if n == 0:
                res.append(lvl_end)
                n = len(q)
        return res