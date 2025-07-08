# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def heightofT(node):
    if node==None:
        return 0 
    left = heightofT(node.left) #here it also looks to left and when bo it reaches the leafnode ,it returns back the value in case of leaf it sends 1 to the upper
    right= heightofT(node.right)# here too it gets the value which accumulates and get the final value when it returns back to the root node and there the comparison happens

    return 1+ max(left,right)
    
    
    




class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            return heightofT(root)
