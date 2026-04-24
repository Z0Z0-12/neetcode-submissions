# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def findHeight(root: Optional[TreeNode]):
            if root == None:
                return 0

            countLeft = 1 + findHeight(root.left)
            countRight = 1 + findHeight(root.right)

            if countLeft > countRight:
                return countLeft
            else:
                return countRight

        if root != None:
            if abs(findHeight(root.right) - findHeight(root.left)) > 1:
                return False
            
            right = self.isBalanced(root.right)
            left = self.isBalanced(root.left)

            return right and left
        return True

        