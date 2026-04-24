# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        countLeft = 1 + self.maxDepth(root.left)
        countRight = 1 + self.maxDepth(root.right)

        if countLeft > countRight:
            return countLeft
        else:
            return countRight