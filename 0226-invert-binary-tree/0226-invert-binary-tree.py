# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def revnode(node):
    if node:
        node.left,node.right=node.right,node.left
        revnode(node.left)
        revnode(node.right)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        revnode(root)
        return root
        
        