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
        return self.balance<=1
    
    