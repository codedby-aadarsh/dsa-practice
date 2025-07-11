# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def isequal(node1,node2):
    if node1 is None and node2 is None:
        return True
    elif node1 is None or node2 is None:
        return False
    elif node1.val!=node2.val :
        return False
    else:
        val1=isequal(node1.left,node2.left)
        val2=isequal(node2.right,node1.right)

    return val1 and val2






class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return isequal(p,q)

        