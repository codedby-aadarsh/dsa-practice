# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balance=0

        def height(node):
            if not node : return 0
            left=height(node.left)
            right=height(node.right)
            self.balance=max(abs(left-right),self.balance)
            return 1+max(left,right)
        height(root)
        return False if self.balance>1 else True
    
    