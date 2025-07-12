def issub(node1,node2):
    if node1 is None and node2 is None:
        return True
    elif node1 is None or node2 is None:
        return False
    elif node1.val!=node2.val:
        return False
    return issub(node1.left,node2.left)and issub(node1.right,node2.right)
    
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
             return True
        elif root is None:
            return False
        if issub(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


        