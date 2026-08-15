# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        elif root1 == None or root2 == None:
            return False
        else:
            if root1.val != root2.val:
                return False
            else:
                return (self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot != None:
            return False
        if self.isSameTree(root, subRoot) == False:
            return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        else:
            return True 
        