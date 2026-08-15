# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree_(self, preorder, pStart, pEnd, inorder, iStart, iEnd):
        if pStart == pEnd:
            return None
        newnode = TreeNode(preorder[pStart])
        inOrdIdx = self.inOrdPos[preorder[pStart]]
        leftTreeSize = inOrdIdx - iStart
        newnode.left = self.buildTree_(preorder, pStart + 1, pStart + leftTreeSize + 1, inorder, iStart, inOrdIdx)
        newnode.right = self.buildTree_(preorder, pStart + leftTreeSize + 1, pEnd, inorder, inOrdIdx + 1, iEnd)
        return newnode

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inOrdPos = {}
        for i, node in enumerate(inorder):
            self.inOrdPos[node] = i
        
        return self.buildTree_(preorder, 0, len(preorder), inorder, 0, len(inorder))
        